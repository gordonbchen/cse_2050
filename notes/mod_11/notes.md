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
        * remove_vertex: O(1), O(E) if you have to remove edges with vertex
        * add_edge: O(1)
        * remove_edge: O(1)
        * get_neighbors: O(E), iterate through all edges, check if source is v,
        * problem: slow to find neighbors

# 11/20/2024
* Graph: set of vertexes V, set of edges E
    * Directed: u -> v
    * Undirected (also doubly directed): u <-> v
    * Degree: # edges in / out
* Graph ADT:
    * add/remove vertex
    * add/remove edge
    * get_neigbors: traverse the graph
* Edge set implementation
    * Stores a set of vertices V, and edges E
    * Problem: iterate through all edges to get neighbors of a single vertex O(E)
* Adjacency set implementation
    * Store a set of vertices V and dictionary of neighbors for each vertex
    * add_vertex: O(1)
    * remove_vertex: O(1), O(E) if you have to remove edges with vertex
    * add_edge: O(1)
    * remove_edge: O(1)
    * get_neighbors: O(1) to get neighbors, O(degree(V)) to iterate through neighbors
* Path: list of verticies with edges inbetween
    * Simple path: no repeated vertices
    * Path length = number of edges
    * Cycle: path where all vertices are distinct, except start vertex = end vertex
* Connectivity
    * Directed
        * Strongly connected: exists a path from every vertex u to v
        * Disconnected graph: multiple graph components
        * Complete / fully connected graph: exists edge from every vertex u to v
    * Undirected:
        * Connected exists path from every vertex u to v
        * Complete: exists edge from every vertex u to v
    * Testing if notes are connected: recursively check if the target is a neighbor, add visited set to prevent recursion error from cycles
