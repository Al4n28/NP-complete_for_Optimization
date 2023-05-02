import numpy as np
import cvxpy as cp
from scipy.linalg import eig, sqrtm


def max_cut_problem(num_nodes, edges):
    A = np.zeros((num_nodes, num_nodes))
    for edge in edges:
        i, j = edge
        A[i, j] = 1
        A[j, i] = 1

    X = cp.Variable((num_nodes, num_nodes), PSD=True)
    constraints = [X[i, i] == 1 for i in range(num_nodes)]
    constraints += [X[i, j] == X[j, i] for i in range(num_nodes) for j in range(i)]
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if A[i, j] == 1:
                constraints += [X[i, i] + X[j, j] - 2*X[i, j] >= 1]
    obj = cp.Maximize(cp.trace(X))

    prob = cp.Problem(obj, constraints)
    prob.solve(solver=cp.SCS)

    # black box
    X_opt = X.value
    eigvals, eigvecs = eig(X_opt)


    smallest_eigval_idx = np.argmin(eigvals)
    smallest_eigvec = eigvecs[:, smallest_eigval_idx]

    # black box to cluster
    cluster = np.zeros(num_nodes)
    for i in range(num_nodes):
        if smallest_eigvec[i] >= 0:
            cluster[i] = 1
        else:
            cluster[i] = -1

    return cluster