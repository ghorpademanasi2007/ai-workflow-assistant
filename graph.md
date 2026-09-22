# Graph Used for BFS and DFS

The graph is an undirected graph with vertices A, B, C, D, E, F and G.

```text
        A
       / \\
      B   C
     / \\   \\
    D   E---F
         \\
          G
```

## Edges

```text
A-B
A-C
B-D
B-E
C-F
E-F
E-G
```

## Adjacency List

```text
A: B, C
B: A, D, E
C: A, F
D: B
E: B, F, G
F: C, E
G: E
```

## Traversals from A

- BFS: A B C D E F G
- DFS: A B D E F C G
