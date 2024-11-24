from typing import Any, Iterator
from queue import Queue


class Graph:
    """ADT for an undirected, unweighted graph."""

    def __init__(self, V: set[Any] = None, E: set[tuple] = None) -> None:
        """Initialize the graph."""
        raise NotImplementedError()

    def __iter__(self) -> Iterator:
        """Return an iterator over all vertices in the graph."""
        raise NotImplementedError()

    def add_vertex(self, v: Any) -> None:
        """Add vertex v to the graph."""
        raise NotImplementedError()

    def add_edge(self, e: tuple) -> None:
        """Add edge e to the graph. Note that this is an undirected graph."""
        raise NotImplementedError()

    def nbrs(self, v: Any) -> Iterator:
        """Return all neighbors of v."""
        raise NotImplementedError()

    def is_connected(self, v1: Any, v2: Any) -> bool:
        """Return True if v1 and v2 are connected."""
        return self._is_connected(v1, v2, visited=set())

    def _is_connected(self, v1: Any, v2: Any, visited: set) -> bool:
        """
        Return True if v1 and v2 are connected.
        v1 is the source node, and v2 is the target node.
        """
        if v1 == v2:
            return True
        if v1 in visited:
            return False

        visited.add(v1)

        for neighbor in self.nbrs(v1):
            if self._is_connected(neighbor, v2, visited):
                return True
        return False

    def bfs(self, v: Any) -> dict:
        """Return a breadth-first search tree mapping nodes to parents."""
        bfs_tree = {}

        to_visit = Queue()
        to_visit.put((None, v))

        while not to_visit.empty():
            src, target = to_visit.get()
            if target in bfs_tree:
                continue

            bfs_tree[target] = src

            for neighbor in self.nbrs(target):
                to_visit.put((target, neighbor))

        return bfs_tree

    def shortest_path(self, v1: Any, v2: Any) -> list:
        """
        Find the shortest path between v1 (src) and v2 (target).
        Return a list of vertices representing the path [v1 ... v2].
        """
        bfs_tree = self.bfs(v1)
        if v2 not in bfs_tree:
            raise ValueError(f"No path exists between {v1} and {v2}.")

        path = [v2]
        while path[-1] != v1:
            path.append(bfs_tree[path[-1]])
        path.reverse()
        return path

    def count_trees(self) -> tuple[list[dict], int]:
        """
        Count the number of trees (isolated graphs) within the overall forest (overall graph).
        Return a list of distinct trees within the graph, and the number of trees.
        """
        trees = []
        visited_vertices = set()
        for v in self:
            if v in visited_vertices:
                continue

            bfs_tree = self.bfs(v)
            trees.append(bfs_tree)

            for unvisited_v in bfs_tree:
                visited_vertices.add(unvisited_v)

        return trees, len(trees)


class EdgeSetGraph(Graph):
    """An undirected graph represented by an edge set."""

    def __init__(self, V: set[Any] = None, E: set[tuple] = None) -> None:
        """Initialize the graph."""
        self._V = set() if V is None else V

        self._E = set()
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __iter__(self) -> Iterator:
        """Return an iterator over all vertices in the graph."""
        return iter(self._V)

    def add_vertex(self, v: Any) -> None:
        """Add vertex v to the graph."""
        self._V.add(v)

    def add_edge(self, e: tuple) -> None:
        """Add edge e to the graph. Note that this is an undirected graph."""
        self._E.add(frozenset(e))

    def nbrs(self, v: Any) -> Iterator:
        """Yield all neighbors of v."""
        for e in self._E:
            edge_tuple = tuple(e)
            if edge_tuple[0] == v:
                yield edge_tuple[1]
            elif edge_tuple[1] == v:
                yield edge_tuple[0]


class AdjacencySetGraph(Graph):
    """An undirected graph represented by an adjacency set."""

    def __init__(self, V: set[Any] = None, E: set[tuple] = None) -> None:
        """Initialize the graph."""
        self._V = set() if V is None else V

        self._adj: dict[Any, set] = {}
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __iter__(self) -> Iterator:
        """Return an iterator over all vertices in the graph."""
        return iter(self._V)

    def add_vertex(self, v: Any) -> None:
        """Add vertex v to the graph."""
        self._V.add(v)

    def add_edge(self, e: tuple) -> None:
        """Add edge e to the graph. Note that this is an undirected graph."""
        v1, v2 = e

        if v1 not in self._adj:
            self._adj[v1] = set()
        self._adj[v1].add(v2)

        if v2 not in self._adj:
            self._adj[v2] = set()
        self._adj[v2].add(v1)

    def nbrs(self, v: Any) -> Iterator:
        """Return all neighbors of v."""
        return iter(self._adj.get(v, []))
