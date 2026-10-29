# AI Lab Experiments

This repository contains the source code and outputs for all 10 AI Lab experiments.

---

## List of Experiments

| Experiment No. | Experiment Name | File Name |
| :--- | :--- | :--- |
| **Experiment 1** | Breadth First Search (BFS) | [`exp1_bfs.py`](exp1_bfs.py) |
| **Experiment 2** | Depth First Search (DFS) | [`exp2_dfs.py`](exp2_dfs.py) |
| **Experiment 3** | Hill Climbing Algorithm | [`exp3_hill_climbing.py`](exp3_hill_climbing.py) |
| **Experiment 4** | A* Algorithm | [`exp4_astar.py`](exp4_astar.py) |
| **Experiment 5** | Min-Max Algorithm | [`exp5_minimax.py`](exp5_minimax.py) |
| **Experiment 6** | Alpha-Beta Pruning | [`exp6_alpha_beta.py`](exp6_alpha_beta.py) |
| **Experiment 7** | 8-Queens Problem | [`exp7_8_queens.py`](exp7_8_queens.py) |
| **Experiment 8** | Water Jug Problem | [`exp8_water_jug.py`](exp8_water_jug.py) |
| **Experiment 9** | Tic-Tac-Toe Game | [`exp9_tic_tac_toe.py`](exp9_tic_tac_toe.py) |
| **Experiment 10** | Travelling Salesman Problem (TSP) | [`exp10_tsp.py`](exp10_tsp.py) |

---

## Experiments & Relevant Outputs

### Experiment 1: Breadth First Search (BFS)
**File:** `exp1_bfs.py`
```
BFS Traversal starting from node A:
A B C D E F 
```

---

### Experiment 2: Depth First Search (DFS)
**File:** `exp2_dfs.py`
```
DFS Traversal starting from node A:
A B D E F C 
```

---

### Experiment 3: Hill Climbing Algorithm
**File:** `exp3_hill_climbing.py`
```
Initial State: x = 0 f(x) = 0
Move to: x = 1 f(x) = 9
Move to: x = 2 f(x) = 16
Move to: x = 3 f(x) = 21
Move to: x = 4 f(x) = 24
Move to: x = 5 f(x) = 25
Peak found at: x = 5 with maximum value f(x) = 25
```

---

### Experiment 4: A* Search Algorithm
**File:** `exp4_astar.py`
```
Running A* Search:
Path found: ['A', 'E', 'D', 'G']
Total Cost: 10
```

---

### Experiment 5: Min-Max Algorithm
**File:** `exp5_minimax.py`
```
Leaf node values: [3, 5, 2, 9, 12, 5, 23, 23]
The optimal value is: 12
```

---

### Experiment 6: Alpha-Beta Pruning
**File:** `exp6_alpha_beta.py`
```
Leaf node values: [3, 5, 6, 9, 1, 2, 0, -1]
The optimal value using Alpha-Beta Pruning is: 5
```

---

### Experiment 7: 8-Queens Problem
**File:** `exp7_8_queens.py`
```
8-Queens Solution Matrix:
1 0 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 
0 1 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 0 1 0 0 
0 0 1 0 0 0 0 0 
```

---

### Experiment 8: Water Jug Problem
**File:** `exp8_water_jug.py`
```
Capacities: Jug A = 4 L, Jug B = 3 L, Target = 2 L
Steps to solve Water Jug Problem:
Jug A: 0 L , Jug B: 0 L
Jug A: 0 L , Jug B: 3 L
Jug A: 3 L , Jug B: 0 L
Jug A: 3 L , Jug B: 3 L
Jug A: 4 L , Jug B: 2 L
```

---

### Experiment 9: Tic-Tac-Toe Game
**File:** `exp9_tic_tac_toe.py`
```
Tic-Tac-Toe Game
  |   |  
--+---+--
  |   |  
--+---+--
  |   |  
Player X places on position 1
X |   |  
--+---+--
  |   |  
--+---+--
  |   |  
Player O places on position 5
X |   |  
--+---+--
  | O |  
--+---+--
  |   |  
Player X places on position 2
X | X |  
--+---+--
  | O |  
--+---+--
  |   |  
Player O places on position 9
X | X |  
--+---+--
  | O |  
--+---+--
  |   | O
Player X places on position 3
X | X | X
--+---+--
  | O |  
--+---+--
  |   | O
Player X wins!
```

---

### Experiment 10: Travelling Salesman Problem (TSP)
**File:** `exp10_tsp.py`
```
Distance Matrix:
[0, 10, 15, 20]
[10, 0, 35, 25]
[15, 35, 0, 30]
[20, 25, 30, 0]
Starting City: 0
Optimal Path: [0, 1, 3, 2, 0]
Minimum Cost: 80
```
