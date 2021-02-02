
import networkx as nx
import osmnx as ox
import requests
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as colors

import re
from num2words import num2words

import csv





#G = ox.graph_from_place('New york city, New York, USA', network_type='drive')

#ox.io.save_graphml(G, filepath='data/ml.graphml', gephi=False, encoding='utf-8')

G = ox.io.load_graphml(filepath='nyc-navigation/data/ml.graphml')

origin_node = ox.get_nearest_node(G, (40.789592,-73.800298)) 
destination_node = ox.get_nearest_node(G, (40.735079,-73.708458))

route2 = ox.shortest_path(G, origin_node, destination_node, weight='length')

fig, ax = ox.plot_graph_route(G, route2, route_color='y', route_linewidth=6, node_size=0)

"""unpacked = [pd.DataFrame({**{'node': node, **data}}, index=[i]) for i, (node, data) in enumerate(G.nodes(data=True))]
df = pd.concat(unpacked)
df.to_csv('data/g.csv')"""

#G = ox.add_edge_speeds(G)

# df = pd.read_csv('nyc-navigation/data/datweight_2.csv')
# edges = pd.read_csv('nyc-navigation/data/edges_new.csv')

# you can convert your graph to node and edge GeoPandas GeoDataFrames
#gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
#gdf_nodes.to_csv('nodes.csv',index=False)
#gdf_edges.to_csv('edges.csv',index=False)
#test = pd.read_csv('data/edges_of_nyc.csv')

#edges = list(G.edges(keys=True, data=True))

#print(edges[1][3]['name']) 

#print(edges['detail']['name'])
'''edges_new = []

fields = ['start_edge','end_edge','niv','name']

for i in range(len(edges)):

    if ('name') in edges[i][3]:
        edges_new.append([edges[i][0], edges[i][1], edges[i][2], edges[i][3]['name']])
    else:
        edges_new.append([edges[i][0], edges[i][1], edges[i][2], 'unknown'])

with open('nyc-navigation/data/edges_new.csv', 'w') as f: 
      
    # using csv.writer method from CSV package 
    write = csv.writer(f) 
      
    write.writerow(fields) 
    write.writerows(edges_new)'''


# df_B=(df.rename(columns={"filtered_street":"name", "WEIGHT":"danger_weight"}))
# df_merged=edges.merge(right=df_B,
#                      how='left', # if an entry is in A, but not in B, add NA values
#                      on=["name"],  # property to merge on
#                     )
# df_merged.fillna(0)

# origin_node = ox.get_nearest_node(G, (40.789592,-73.800298)) 
# destination_node = ox.get_nearest_node(G, (40.735079,-73.708458))

# nx.set_edge_attributes(G, 0, 'danger_weight')
# route1 = ox.shortest_path(G, origin_node, destination_node, weight='danger_weight')
# route2 = ox.shortest_path(G, origin_node, destination_node, weight='length')
# route = [route1, route2]
# color = ['y' , 'r']
# fig, ax = ox.plot_graph_routes(G, route, route_colors=color, route_linewidth=6, node_size=0)

'''df = pd.read_csv('nyc-navigation/data/datweight.csv')

substr = r'^\d+'

a = []
for i in range(df.shape[0]):
    value = re.findall(substr, df['filtered_street'][i])
    value = ''.join(value)
    a.append(value)

#print(num2words(a[4], to='ordinal_num'))       #to_replace=r'^ba.$', value='new', regex=True

for i in range(len(a)):
    if a[i]:
        a[i] = num2words(a[i], to='ordinal_num')
        

for i in range(df.shape[0]):

    if a[i]:
        df['filtered_street'][i] = re.sub(substr, a[i], df['filtered_street'][i])
        
df.to_csv('nyc-navigation/data/datweight_2.csv')

#df['filtered_street'][0] = df['filtered_street'][0].replace(substr, num2words(df['filtered_street'][0].findall(substr)), to='ordinal_num'), regex=True)
#print(df)'''
