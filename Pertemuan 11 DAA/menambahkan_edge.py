class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def edges(self):
        return self.findedges()

    def AddEdge(self,edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

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
    "V" : ["U", "X"],
    "W" : ["T","X","Z"],
    "X" : ["V", "W", "S"],
    "Z" : ["W"],
    "S" : ["X"]
}

graph_elements_tiga = {
    "R" : ["O","L"],
    "O" : ["R", "M"],
    "M" : ["O", "N"],
    "L" : ["R","P"],
    "P" : ["L","N"],
    "N" : ["M","P"]
}

g = graph(graph_elements)
g2 = graph(graph_elements_dua)
g3 = graph(graph_elements_tiga)
g.AddEdge({"a", "e"})
g.AddEdge({"a", "c"})
g2.AddEdge({"T", "V"})
g2.AddEdge({"X", "U"})
g3.AddEdge({"R", "N"})
g3.AddEdge({"P", "O"})
print(g.edges())
print(g2.edges())
print(g3.edges())