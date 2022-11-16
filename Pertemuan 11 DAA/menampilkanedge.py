class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def edges(self):
        return self.findedges()
    #find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
#create the dictionary with graph elements
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
print(g.edges())
print(g2.edges())
print(g3.edges())
    