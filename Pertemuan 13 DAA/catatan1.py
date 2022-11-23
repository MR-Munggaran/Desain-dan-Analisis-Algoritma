def bfs(graph,start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours : 
                queue.append(neighbour)
    return visited

graph = {
    "Amin"  : {"Wasim","Nick","Mike"},
    "Wasim" : {"Imran", "Amin"},
    "Imran" : {"Wasim","Faras"},
    "Faras" : {"Imran"},
    "Mike"  : {"Amin"},
    "Nick"  : {"Amin"}
}

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

print(bfs(graph,"Amin"))
print(bfs(graph,"Wasim"))
print(bfs(graph,"Imran"))

print(bfs(graph_lain,"Rektor"))
print(bfs(graph_lain,"Warek 1"))
print(bfs(graph_lain,"Warek 2"))
print(bfs(graph_lain,"Dosen G"))

