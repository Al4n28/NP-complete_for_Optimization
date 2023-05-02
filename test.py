
from max_cut import max_cut_problem
import time
import csv

txt_name = "max_nodes100_max_edges4950"
num_nodes = 100

with open(txt_name+".txt", "r") as f:
    graphs = [eval(line.strip()) for line in f]

with open('result_'+txt_name+'.csv', "w", newline='') as r_f:
    writer = csv.writer(r_f)
    writer.writerow(["Num Nodes", "Num Edges", "Time Taken", "Cluster"])

    for g in graphs:
        start_time = time.time() 
        cluster = max_cut_problem(num_nodes,g)
        end_time = time.time() 

        num_edges = len(g)
        writer.writerow([num_nodes, num_edges, end_time - start_time,cluster])


