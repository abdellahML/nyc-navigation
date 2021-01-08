
import networkx as nx
import osmnx as ox
import requests
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as colors


G = ox.graph_from_place('New york city, New York, USA', network_type='drive')
#G = ox.add_edge_speeds(G)

# you can convert your graph to node and edge GeoPandas GeoDataFrames
#gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
#gdf_nodes.to_csv('nodes.csv',index=False)
#gdf_edges.to_csv('edges.csv',index=False)
#test = pd.read_csv('data/edges_of_nyc.csv')
edges = list(G.edges(keys=True, data=True))
print(edges[0][3]['highway'])