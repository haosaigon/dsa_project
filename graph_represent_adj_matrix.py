import networkx as nx
import matplotlib.pyplot as plt

def createAdjacencyMatrix(vertices, edges):
    noofvertices = len(vertices)
    adjM = []
    while(len(adjM) < noofvertices):
        temp = []
        for i in range(noofvertices):
            temp.append(0)
        adjM.append(temp)
    for edge in edges:
        i = edge[0]
        j = edge[1]
        if i >= noofvertices or j >= noofvertices or i < 0 or j < 0:
            print(f"Not a Proper Input in Edge {i},{j}")
        else:
            adjM[i][j] = 1
            adjM[j][i] = 1
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()
    return adjM

# Example usage:
vertices = [0, 1, 2, 3]
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
adjM = createAdjacencyMatrix(vertices, edges)
print(adjM)
case = 100
matrix_time = timeit.timeit(lambda: adjM, number=case)
print() #Print empty line to look nice
print("DFS time:", matrix_time)
