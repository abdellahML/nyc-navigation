import pandas as pd
import numpy as np

import networkx as nx
import osmnx as ox

from typing import Type

class Preprocessing:
    """In this class we will prepare our dataset before tracing our path on ny_map_osmnx.py
    the main objective is to have a data group by street name and each street with a danger weight"""

    def import_csv_file(self, csv_file: str):
        """This function will import our data as dataframe and return a variable dataframe"""

        df = pd.read_csv(csv_file)
        return df
    
    def create_edge_csv_file(self, edges, path):
        """This function will create a new csv file if we we give it values to write on it
        for now it's not general but if i have times i will change it"""

        edges_new = []

        fields = ['start_edge','end_edge','niv','name']

        for i in range(len(edges)):

            if ('name') in edges[i][3]:
                edges_new.append([edges[i][0], edges[i][1], edges[i][2], edges[i][3]['name']])
            else:
                edges_new.append([edges[i][0], edges[i][1], edges[i][2], 'unknown'])

        with open(path, 'w') as f: 
            
            # using csv.writer method from CSV package 
            write = csv.writer(f) 
            
            write.writerow(fields) 
            write.writerows(edges_new)

    
    def add_danger_weight(self, G, origin, destination, crash):
        """This function will create a  new column in our dataframe which is the weight of danger for each street,
        it will be based on the number of accident by street and will return the changed dataframe"""
        
        G = ox.graph_from_place('New york city, New York, USA', network_type='drive')
        df = self.import_csv_file('nyc-navigation/data/datweight.csv')

        edges_list = list(G.edges(keys=True, data=True))
        self.create_edge_csv_file(edges=edges_list, path='nyc-navigation/data/edges_new.csv')
        edges = self.import_csv_file('nyc-navigation/data/edges_new.csv')

        df_B=(df.rename(columns={"on_street_name":"name", "SUM":"danger_weight"}))
        df_merged=edges.merge(right=df_B,
                            how='left', # if an entry is in A, but not in B, add NA values
                            on=["name"],  # property to merge on
                            )
        df_merged.fillna(0)

        return df_merged

