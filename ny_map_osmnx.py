import networkx as nx
import osmnx as ox
import requests
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as colors


####Create a class path who will define our function for the project.
### Our class should take as parameter the origin and destination at least

### Our first function should check the type of destination  and origin is it coordinate or string ? then dispatch to the right function.
### second function and third should check if the given origin/destination are in a df that i will create with all street of NYC if not return error
### else if it exist we should check for the safest path ( maybe call another function to keep it short)
## Your should return the plot of the path for the template(safest_path.html) it's already waiting for the response
place = 'New york city,New York, USA'
G = ox.graph_from_place(place, network_type='drive')

class NYMapOSMnx:
    def __init__(self):
        self.origin = origin
        self.destination = destination
        self.df = pd.read_csv('data/edges_of_nyc.csv')
   ## self.G = ox.graph_from_place(place, network_type='drive') do we need this ? 

    def creat_graph(self, place: str):
        """This function will create the graph of New York and return it"""
        place = 'New york city,New York, USA'
        G = ox.graph_from_place(place, network_type='drive')
        return G




    def isPresent(self,origin,destination):
        if origin in self.df.name and destination in self.df.name :
            ## call getSafest
            return True
        elif origin not in self.df.name:
            return False
        elif destination not in self.df.name:
            return False

    def safest_way(origin,destination):                                                                 # select safest route
        route = ox.shortest_path(G, origin, destination, weight='danger_weight')
        fig, ax = ox.plot_graph_route(G, route, route_color='y', route_linewidth=6, node_size=0)        # plot the safest road
        route_risk = int(sum(ox.utils_graph.get_route_edge_attributes(G, route, 'danger_weight')))      # print the risk on this road
        txt1 = 'The risk on this Route is ' 
        txt2 =  ' accidents per year'
        return fig,txt1,txt2,route_risk

place = 'New york city,New York, USA'
G = ox.graph_from_place(place, network_type='drive')
print(G.head(100))
