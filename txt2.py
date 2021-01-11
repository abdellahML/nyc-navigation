import networkx as nx
import osmnx as ox
import requests
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as colors

place = 'New york city,New York, USA'
G = ox.graph_from_place(place, network_type='drive')
print(G)