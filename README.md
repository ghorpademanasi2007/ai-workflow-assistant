# BFS and DFS Graph Traversal with Py-Spy

## Project Overview

This project demonstrates two fundamental graph traversal algorithms:

- **BFS (Breadth-First Search)** – visits vertices level by level using a queue.
- **DFS (Depth-First Search)** – explores as far as possible along a branch before backtracking, using recursion.

The programs are written in Python and can be profiled using **py-spy** to observe where execution time is spent.

## Graph Used

The same graph is used for both BFS and DFS:

```text
        A
       / \\
      B   C
     / \\   \\
    D   E---F
         \\
          G
```

Edges:
- A-B
- A-C
- B-D
- B-E
- C-F
- E-F
- E-G

## Files

```text
ai-workflow-assistant/
│
├── BFS.py
├── DFS.py
├── graph.md
├── README.md
├── CONTRIBUTION_LOG.md
└── ADR.md
```

## How to Run

Open Git Bash in the project folder and run:

```bash
python BFS.py
python DFS.py
```

Expected traversal for the graph above:

```text
BFS: A B C D E F G
DFS: A B D E F C G
```

## Py-Spy Profiling

Install py-spy:

```bash
python -m pip install py-spy
```

Check installation:

```bash
py-spy --version
```

Run BFS profiling:

```bash
py-spy record -o BFS_profile.svg -- python BFS.py
```

Run DFS profiling:

```bash
py-spy record -o DFS_profile.svg -- python DFS.py
```

The generated `.svg` files are flame graphs showing the time spent in different parts of the program.

If `py-spy` is not recognized, use the full executable path returned by:

```bash
python -m pip show py-spy
```

## Time Complexity

For an adjacency-list graph:

| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| BFS | O(V + E) | O(V + E) | O(V + E) | O(V) |
| DFS | O(V + E) | O(V + E) | O(V + E) | O(V) |

Here, **V** is the number of vertices and **E** is the number of edges.

## Tools Used

- Python
- Git
- GitHub
- Visual Studio Code
- py-spy

## Learning Outcome

This activity helps understand graph traversal, queue/recursion based searching, algorithm complexity, and basic performance profiling with py-spy.
