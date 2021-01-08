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

        crash = pd.read_csv(csv_file)
        return crash
    
    def add_danger_weight(self, G, origin, destination, crash):
        """This function will create a  new column in our dataframe which is the weight of danger for each street,
        it will be based on the number of accident by street and will return the changed dataframe"""
        G = ox.graph_from_place('New york city, New York, USA', network_type='drive')
        gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
        df = self.import_csv_file('nyc-navigation/data/datweight.csv')

        return G

G = ox.graph_from_place('New york city, New York, USA', network_type='drive')
df = Preprocessing().import_csv_file('nyc-navigation/data/datweight.csv')
df = df.rename(columns={'on_street_name':'name', 'SUM':'danger_weight'})

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
gdf_edges['danger_weight'] = 0

#gdf_edges['danger_weight'] = gdf_edges.name.map(df.set_index('on_street_name')['SUM']).reset_index()

for i in range(df.shape[0]):

    gdf_edges.loc[gdf_edges['name'] == df.at[i,'name'], 'name'] = df.at[i, 'danger_weight']

gdf_edges.to_csv('edges_new.csv',index=False)
'''
df = Preprocessing().import_csv_file('edges_new.csv')
print(df['danger_weight'])'''

