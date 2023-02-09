#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Laurent FERHI   
# Created Date: 2023-02-09
# version = 4.0
# ---------------------------------------------------------------------------

"""
This module provides a simple ant colony optimization technique to find optimal
solutions to travelling salesman types of problems. Input is a distance matrix
between all the nodes (diagonal at np.inf) to avoid staying in the same node.
Output is a pandas.DataFrame containing the best solutions and their associated
distance.

Algorithm is based on rational developed in:
M. Dorigo and T. Stützle, "Ant Colony Optimization," 
MIT Press, Cambridge, 2004, ISBN-0-262-04219-3
"""

import sys
import numpy as np
import itertools
from datetime import datetime
import pandas as pd

def progressbar(it, prefix="", size=60, out=sys.stdout):
    '''
    https://stackoverflow.com/questions/3160699/python-progress-bar
    '''
    count = len(it)
    def show(j):
        x = int(size*j/count)
        out.write("%s[%s%s] %i/%i\r" % (prefix, u"#"*x, "."*(size-x), j, count))
        out.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    out.write("\n")
    out.flush()

def ACO(dist_matrix, n_ants, n_best, n_iter, alpha, beta, decay):
    
    ### Embedded functions
    
    def select_next_node(ph_matrix, dist, visited):
        '''
        Calculate proba to go on next nodeon a ph matrix copy with 
        visited nodes ph=0 to avoid going back to already visited nodes
        '''
        ph_matrix = np.copy(ph_matrix) 
        for node in list(visited):
            ph_matrix[node] = 0

        # Random choice with weighted proba
        score = ph_matrix**alpha*((1/dist)**beta)
        next_node = np.random.choice(range(len(dist_matrix)), size=1, p=score/score.sum())[0]
        
        return next_node

    def ant_exploration(start):
        '''
        Explore and remember 1 path. Path ~ list(tuples): [(0,2),(2,4),(4,7)]
        Used to get distance and deposite pheromone more easily
        '''
        path = []
        visited = set() # memory to update each time a node is visited
        
        node = start
        visited.add(start)
        
        for _ in range(len(dist_matrix) - 1):
            next_node = select_next_node(ph_matrix[node], dist_matrix[node], visited)
            path.append((node, next_node))
            node = next_node
            visited.add(next_node)
            
        #path.append((node, start)) # return to start node (optional)
        
        return path

    ### Main loop
    
    start_node = 0 # Default: start from upper left corner
    ph_matrix = np.ones(dist_matrix.shape) / len(dist_matrix) # initializing ph_matrix
    print_every = 10 # print every x iterations
    print('> Ants are colonizing...')
    
    for epoch in progressbar(range(n_iter),"  Epoch: ", 50):
        
        # Explore all paths
        paths_list = []
        for _ in range(n_ants):
            path = ant_exploration(start=start_node)
            paths_list.append((path, sum([dist_matrix[x] for x in path])))

        # Update pheromon matrix on n_best paths
        for path, dist in sorted(paths_list, key=lambda x: x[1])[:n_best]:
            for coord in path:
                ph_matrix[coord] += 1/dist_matrix[coord]
                        
        # Apply decay to pheromone matrix
        ph_matrix *= decay 

    # Put results in df with path: [(0,2),(2,4),(4,7)] --> 0 2 4 7 and distance
    df_paths = pd.DataFrame(paths_list, columns=['path','distance'])
    df_results = df_paths['path']\
        .apply(lambda x: [k[0] for k in itertools.groupby(list(itertools.chain(*x)))])\
        .apply(pd.Series)
    df_results['distance'] = df_paths['distance']
    print('> Ants found their way !')
    
    return df_results.drop_duplicates().sort_values('distance')

if __name__ == "__main__":
    
    # Random symmetrical matrix
    N = 10
    rd_mx = np.random.uniform(0,20,size=(N,N))
    X = (rd_mx + rd_mx.T)
    X[np.diag_indices_from(X)] = np.inf
    print("Distance Matrix:")
    print(pd.DataFrame(X).applymap(lambda x: round(x,1)))
    print()

    solutions = ACO(X, n_ants=50, n_best=50, n_iter=100, alpha=1, beta=1.6, decay=0.9)
    print()
    print("Best paths:")
    for idx in range(solutions.shape[0]):
        path = solutions.drop('distance',axis=1).iloc[idx].tolist()
        distance = solutions.iloc[idx]['distance']
        print('Path: {}, Distance: {:.2f}'.format(' '.join(map(str,path)), distance))
