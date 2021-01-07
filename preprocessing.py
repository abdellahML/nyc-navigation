import pandas as pd
import numpy as np

class Preprocessing:
    """In this class we will prepare our dataset before tracing our path on ny_map_osmnx.py
    the main objective is to have a data group by street name and each street with a danger weight"""

    def import_csv_fil(self, csv_file: str):
        """This function will import our data as dataframe"""

        crash = pd.read_csv(csv_file)
        return crash
    
    