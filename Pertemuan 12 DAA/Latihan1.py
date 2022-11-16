import networkx as nx
import matplotlib.pyplot as plt

#Buat network
# Hubungkan sebagai berikut: 

# vertices = range(1,10)
edges = [("Mk","Em"), ("Mk","B"), ("B","Jl"), ("Em","Jl"), ("Jh","Jl"), ("Sh","Jl"), ("Lh","Jl"), ("Em","Lz"), ("Sh","Lz"), ("Lz","Al"),("Al","Ls"),("B","Em"),("Em","Sh"),("Sh","Jh"),("Jh","B"),("B","Sh"),("Jh","Em"),("Lh","Sh"),("Lh","Jh")]

G = nx.Graph()
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='r',node_size=800)
#Menampilkan Gambar grafik
centrality = nx.eigenvector_centrality(G)
sorted((v,'{:0.2f}'.format(c))for v,c in centrality.items())
print(centrality)
# print("-"*50)
plt.show()