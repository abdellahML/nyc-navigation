import networkx as nx
import osmnx as ox
import requests
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as colors

place = 'New york city,New York, USA'
G = ox.graph_from_place(place, network_type='drive')

def safest_way(origin,destination):                                                                 # select safest route
    route = ox.shortest_path(G, origin, destination, weight='danger_weight')
    fig, ax = ox.plot_graph_route(G, route, route_color='y', route_linewidth=6, node_size=0)        # plot the safest road
    route_risk = int(sum(ox.utils_graph.get_route_edge_attributes(G, route, 'danger_weight')))      # print the risk on this road
    txt1 = 'The risk on this Route is ' 
    txt2 =  ' accidents per year'
    return fig,txt1,txt2,route_risk


orig = list(G)[0]
dest = list(G)[120]
safest_way(orig,dest)

