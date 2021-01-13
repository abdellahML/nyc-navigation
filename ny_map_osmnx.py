import networkx as nx
import osmnx as ox
import requests
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.cm as cm
import matplotlib.colors as colors
from shapely.geometry import LineString, mapping
import json
from ipyleaflet import *



####Create a class path who will define our function for the project.
### Our class should take as parameter the origin and destination at least

### Our first function should check the type of destination  and origin is it coordinate or string ? then dispatch to the right function.
### second function and third should check if the given origin/destination are in a df that i will create with all street of NYC if not return error
### else if it exist we should check for the safest path ( maybe call another function to keep it short)
## Your should return the plot of the path for the template(safest_path.html) it's already waiting for the response
place = 'New york city,New York, USA'
center = (40.7127837,-74.0059413)
##G = ox.graph_from_place(place, network_type='drive')

class NYMapOSMnx:

    def __init__(self):
        self.df = pd.read_csv('data/edges_of_nyc.csv')
   ## self.G = ox.graph_from_place(place, network_type='drive') do we need this ? 


    def creat_graph(self, place: str):
        """This function will create the graph of New York and return it"""

        place = 'New york city, New York, USA'
        G = ox.graph_from_place(place, network_type='drive')
        return G



    def isPresent(self, origin, destination):
        
        if origin in self.df.name and destination in self.df.name :
            ## call getSafest
            return True
        elif origin not in self.df.name:
            return False
        elif destination not in self.df.name:
            return False


    def safest_way(self, origin, destination, short=False):                                             # select safest route

        a,b = origin
        print(origin)
        print(type(a))
        print(destination)
        #We create a graphml file and save every node/edges in it then with with this line we just load it
        G = ox.io.load_graphml(filepath='data/ml.graphml')
        
        origin_node = ox.get_nearest_node(G, origin)
        destination_node = ox.get_nearest_node(G, destination)

        nx.set_edge_attributes(G, 0, 'danger_weight')

        route1 = ox.shortest_path(G, origin_node, destination_node, weight='danger_weight')
        route_risk = int(sum(ox.utils_graph.get_route_edge_attributes(G, route1, 'danger_weight')))              # print the risk on this road
        txt = 'The risk on this Route is {} accidents per year'.format(route_risk)

        if short:

            route2 = ox.shortest_path(G, origin_node, destination_node, weight='length')                                   #shortest road
            route = [route1, route2]
            colors = ['r', 'y']
            #fig, ax = ox.plot_graph_routes(G, route, route_colors=colors, route_linewidth=6, node_size=0)
            return route1,route2       # plot the safest road

        else:
            
            #fig, ax = ox.plot_graph_route(G, route=route1, route_color='r',route_linewidth=6, node_size=0)
            long = [] 
            lat = []  
            for i in route1:
                point = G.nodes[i]
                long.append(point['x'])
                lat.append(point['y'])
            return long,lat

origin = {'lat': 40.89, 'lng': 45.8788}
print(origin['lat'], origin['lng'])
