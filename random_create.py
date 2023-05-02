import random

graphs = []

# Define the maximum number of nodes and edges
max_nodes = 10
max_edges = 10

# Generate a random graph for each number of nodes and edges
for n in range(1, max_nodes + 1):
    for m in range(n, min(n*(n-1)//2, max_edges) + 1):
        # Create the edges randomly
        edges = set()
        while len(edges) < m:
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            if i != j:
                e = tuple(sorted((i, j)))
                edges.add(e)
        
        # Create the graph and append it to the list
        G = [n, list(edges)]
        graphs.append(G)

# Shuffle the list of graphs
random.shuffle(graphs)
print(graphs)
with open('max_nodes'+str(max_nodes)+'_max_nodes'+str(max_edges)+'.txt', 'w') as file:
    for graph in graphs:
        file.write(f'{graph}\n')