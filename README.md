# Ant Colony Optimization

This module provides a simple ant colony optimization technique to find optimal
solutions to travelling salesman types of problems. Input is a distance matrix
between all the nodes (diagonal at np.inf) to avoid staying in the same node.
Output is a pandas.DataFrame containing the best solutions and their associated
distance.

Algorithm is based on rational developed in:
M. Dorigo and T. Stützle, "Ant Colony Optimization," 
MIT Press, Cambridge, 2004, ISBN-0-262-04219-3

Distance Matrix:
|  |    0 |    1 |    2|     3|    4 |    5 |    6 |    7 |    8  |   9|
|---|---|---|---| ---|---|---|---|--- |---|---|
|0 |  inf | 21.7 |  3.4|  12.6| 17.8 | 23.7 | 25.6 | 23.4 |  3.0  | 1.4|
|1 | 21.7 |  inf | 14.2|  22.5|  5.4 | 24.4 | 18.9 |  9.1 |  9.0  |33.6|
|2 |  3.4 | 14.2 |  inf|  24.4| 25.3 | 17.3 | 35.2 | 15.4 |  7.6  |32.5|
|3 | 12.6 | 22.5 | 24.4|   inf| 18.3 | 38.8 | 25.3 | 25.3 |  7.8  |22.8|
|4 | 17.8 |  5.4 | 25.3|  18.3|  inf | 35.5 | 35.1 | 22.5 | 11.8  |16.1|
|5 | 23.7 | 24.4 | 17.3|  38.8| 35.5 |  inf | 25.9 |  9.2 | 26.8  |16.7|
|6 | 25.6 | 18.9 | 35.2|  25.3| 35.1 | 25.9 |  inf | 22.5 | 14.8  |15.6|
|7 | 23.4 |  9.1 | 15.4|  25.3| 22.5 |  9.2 | 22.5 |  inf | 28.8  |24.3|
|8 |  3.0 |  9.0 |  7.6|   7.8| 11.8 | 26.8 | 14.8 | 28.8 |  inf  |17.6|
|9 |  1.4 | 33.6 | 32.5|  22.8| 16.1 | 16.7 | 15.6 | 24.3 | 17.6  | inf|

> Ants are colonizing...<br/><br/>
  Epoch: [##################################################] 100/100<br/><br/>
> Ants found their way !<br/><br/>

Best paths:
Path: 0 9 6 8 3 4 1 7 5 2, Distance: 98.85
Path: 0 9 4 1 7 5 2 8 3 6, Distance: 99.19
Path: 0 9 6 7 5 2 8 3 4 1, Distance: 105.01
Path: 0 9 6 1 7 5 2 8 3 4, Distance: 105.20
Path: 0 9 5 2 8 3 4 1 7 6, Distance: 106.03
Path: 0 9 5 7 6 8 3 4 1 2, Distance: 110.21
Path: 0 9 6 8 2 7 5 1 4 3, Distance: 112.02
Path: 0 9 6 1 4 8 3 7 5 2, Distance: 112.71
Path: 0 9 5 2 8 3 6 7 1 4, Distance: 113.04
Path: 0 9 8 3 4 1 7 5 2 6, Distance: 121.30
Path: 0 9 5 2 8 3 6 1 4 7, Distance: 122.90
Path: 0 9 6 8 2 1 7 5 3 4, Distance: 128.96

