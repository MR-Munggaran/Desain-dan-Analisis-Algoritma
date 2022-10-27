from ast import increment_lineno
from multiprocessing import connection
import matplotlib
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import C2

# myWeb = nx.DiGraph() #lat 1
# myWeb = nx.path_graph(0) #nomor 3
# myWeb = nx.path_graph(4)nomor2 
# myWeb = nx.path_graph(4) 
# myWeb = nx.lollipop_graph(4,3)#random
# myWeb = nx.path_graph(4) #tigasegi
# myWeb = nx.bipartite.gnmk_random_graph(3,5,10,seed=123)#gagal
myWeb = nx.complete_multipartite_graph(1,2,3,2,1)
# myWeb = nx.path_graph(4)
myPage = range(1,5)
# connections = [(1,3),(2,1),(2,3),(3,1),(3,2),(3,4),(4,5),(5,1),(5,4)] #contoh soal
#connections = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1)] #lat_soal nmr 1
#connections = [(1,2),(2,3),(3,4),(4,5),(5,1)] #lat_soal nmr 2
# connections = [(1,2),(2,3),(3,4),(4,3),(3,2),(2,1)] #lat_soal nmr 3
#connections = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1)] #lat_soal nmr 4
#connections = [(1,2),(2,3),(3,4),(2,1),(3,2),(4,3),(4,1)] #lat_soal nmr 5
#connections = [(1,2),(2,3),(3,4),(4,5),(5,1),(4,1)] #lat_soal nmr 6
connections = [(1,2), (2,3), (3,4),(4,5)]
myWeb.add_nodes_from(myPage)
myWeb.add_edges_from(connections)

# pos=nx.kamada_kawai_layout(myWeb) #nomor3
# pos=nx.shell_layout(myWeb)#lat 1
# pos=nx.spring_layout(myWeb)nomor2
# pos=nx.spectral_layout(myWeb)
# pos=nx.random_layout(myWeb)#random
# pos=nx.planar_layout(myWeb)#segitga
# top = nx.bipartite.sets(myWeb)#gagal
# pos = nx.bipartite_layout(myWeb,top)#gagal
pos = nx.multipartite_layout(myWeb)
# pos = nx.spiral_layout(myWeb)
nx.draw(myWeb, pos, arrows=True, with_labels=True)
# nx.draw(myWeb, pos=pos)
plt.show()

G,p = C2.createPagerank(myWeb)
print(G,p)
