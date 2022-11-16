class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
        # get the keys of the dict
    def getVertice(self):
        return list(self.gdict.keys())

# create the dictionary with graph elements

graph_elements = {
    "a" : ["b","c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}

graph_elements_dua = {
    "T" : ["U","W"],
    "U" : ["T", "V"],
    "V" : ["U", "X"]
}

graph_elements_tiga = {
    "R" : ["O","L"],
    "O" : ["R", "M"],
    "M" : ["O", "N"]
}
g = graph(graph_elements)
g2 = graph(graph_elements_dua)
g3 = graph(graph_elements_tiga)
print(g.getVertice())
print(g2.getVertice())
print(g3.getVertice())

