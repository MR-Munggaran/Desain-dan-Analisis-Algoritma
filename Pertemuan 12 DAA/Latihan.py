import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1,10)
edges = [(6,9),(6,7),(6,14),(6,8),(6,2),(2,12),(2,11),(2,15),(2,1),(1,4),(1,10),(2,3),(3,5),(3,13)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='grey',node_size=800)


# print("-"*50)
# print(nx.degree_centrality(G))
# print("-"*50)
# print(nx.betweenness_centrality(G))
# print("-"*50)
# print(nx.closeness_centrality(G))
# print("-"*50)
centrality = nx.eigenvector_centrality(G)
sorted((v,'{:0.2f}'.format(c))for v,c in centrality.items())
print(centrality)
# print("-"*50)
plt.show()