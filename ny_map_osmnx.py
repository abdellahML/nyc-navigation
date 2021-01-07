import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors


class NYMapOSMnx:
    """This class will create the edge graph of New York and will find the shortest and least dangerous route from a to b"""

    def creat_graph(self, place: str):
        """This function will create the graph of New York and return it"""
        place = 'New york city,New York, USA'
        G = ox.graph_from_place(place, network_type='drive')
        return G

    def getSafest(self, G, origin, destination):
        """This function will give the shortest path with less danger and return it"""

        route = ox.shortest_path(G, origin, destination, weight='lenght')

        return route
    #fig, ax = ox.plot_graph_route(G, route, route_color='y', route_linewidth=6, node_size=0)

    # convert your MultiDiGraph to an undirected MultiGraph
    #M = ox.get_undirected(G)
    # convert your MultiDiGraph to a DiGraph without parallel edges
    #D = ox.get_digraph(G)
    #fig, ax = ox.plot_graph(G,node_size=0, edge_linewidth=0.5)