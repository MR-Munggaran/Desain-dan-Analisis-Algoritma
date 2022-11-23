def dfs (graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited : 
        dfs(graph, next,visited)
    return visited

graph = {
    "Amin"  : {"Wasim","Nick","Mike"},
    "Wasim" : {"Imran", "Amin"},
    "Imran" : {"Wasim","Faras"},
    "Faras" : {"Imran"},
    "Mike"  : {"Amin"},
    "Nick"  : {"Amin"}
}

print(dfs(graph,"Amin"))
# print(dfs(graph,"Wasim"))
# print(dfs(graph,"Imran"))

graph_lain = {
    'Rektor'    : {'Warek 1', 'Warek 2'},
    'Warek 1'   : {'Rektor'},
    'Warek 2'   : {'Rektor', 'Kaprodi 1', 'Kaprodi 2', 'Kaprodi 3'},
    'Kaprodi 1' : {'Dosen A', 'Dosen B', 'Dosen C', 'Warek 2'},
    'Kaprodi 2' : {'Warek 2', 'Dosen D', 'Dosen E'},
    'Kaprodi 3' : {'Warek 2', 'Dosen F', 'Dosen G'},
    'Dosen A'   : {'Kaprodi 1'},
    'Dosen B'   : {'Kaprodi 1'},
    'Dosen C'   : {'Kaprodi 1'},
    'Dosen D'   : {'Kaprodi 2'},
    'Dosen E'   : {'Kaprodi 2'},
    'Dosen F'   : {'Kaprodi 3'},
    'Dosen G'   : {'Kaprodi 3'}
}

# print(dfs(graph_lain,"Rektor"))
# print(dfs(graph_lain,"Warek 1"))
print(dfs(graph_lain,"Warek 2"))
# print(dfs(graph_lain,"Dosen G"))