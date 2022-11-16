#a -------- b
#/
#/
#c ---------d -------- e

#create the dict with graph elements
graph = {
    "a" : ["b","c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}

#print the graph -------->
print(graph)