# T --------- U ----- V
# |                   |
# W ----------------- X
# |                   |
# Z                   S

graph = {
    "T" : ["U","W"],
    "U" : ["T", "V"],
    "V" : ["U", "X"],
    "W" : ["T","X","Z"],
    "X" : ["V", "W", "S"],
    "Z" : ["W"],
    "S" : ["X"]
}

print(graph)