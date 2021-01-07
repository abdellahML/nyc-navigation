import pandas as pd
import numpy as np

from typing import Type

class Preprocessing:
    """In this class we will prepare our dataset before tracing our path on ny_map_osmnx.py
    the main objective is to have a data group by street name and each street with a danger weight"""

    def import_csv_file(self, csv_file: str) --> Type(dataframe):
        """This function will import our data as dataframe"""

        crash = pd.read_csv(csv_file)
        return crash
    
    def add_danger_weight(self, origin: Type(float, float), destination: Type(float, float), crash: Type(dataframe)) --> Type(dataframe):
        """This function will create a  new colonne in our dataframe which is the weight of danger for each street,
        it will be based on the number of accident by street"""

        crash['danger_weight'] = crash['number_of_accident']

        return crash
