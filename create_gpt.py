import random

# Define a function to generate a random graph
def generate_graph(num_nodes, max_edges):
    graph = []
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if len(graph) >= max_edges:
                break
            if random.random() <= max_edges / (num_nodes * (num_nodes - 1) / 2):
                graph.append((i,j))
                if len(graph) >= max_edges:
                    break
        else:
            continue
        break
    return graph

# Create a list of 10 random graphs
num_nodes = 100
max_edges = 4950
graphs = []
for i in range(10):
    G = generate_graph(num_nodes, max_edges)
    graphs.append(G)

# Save the list of graphs to a file
with open('max_nodes'+str(num_nodes)+'_max_edges'+str(max_edges)+'.txt', "w") as f:
    for G in graphs:
        f.write(str(G) + "\n")
