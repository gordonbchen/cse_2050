# 11/18/2024
* Tree: connected, acyclic graph
* Forest: disconnected graphs
* Graph G = (V, E), set of verticies V and set of Edges E
* Edge = tuple(V1, V2)
    * V2 is a neighbor to V1. V1 and V2 are adjacent
    * V1 and V2 are incident to edge e
* Undirected graph
    * Order of verticies in an edge doesn't matter, represent with set
    * Degree: # edges connected to vertex
* Directed graph (digraph)
    * Order of verticies in an edge matters
    * (V1, V2) means V1 -> V2, not V1 <-> V2
    * Represent edge with tuple
    * In-degree: # edges pointing into vertex
    * Out-degree: # edges pointing out of vertex
* Simple graph: no self-loops and multiple edges
    * Self-loop: edges that start and end at the same vertex
    * Multiple edges b/t same pair of verticies
* Graph ADT:
    * \_\_init\_\_(V, E)
    * add_vertex(V), remove_vertex(V)
    * add_edge(u, v), remove_edge(u, v)
    * neighbors(v): returns an iterable of v's neighbors
* Graph ADT implementations
    * Edge set: store a set of verticies V and a set of edges E
        * add_vertex: O(1)
        * remove_vertex: O(E), iterate through edges, removing edges with vertex
        * add_edge: O(1)
        * remove_edge: O(1)
        * get_neighbors: O(E), iterate through all edges, check if source is v,
        * problem: slow to find neighbors
