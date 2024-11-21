from typing import Iterator


class Graph_ES:
    """An edge set digraph."""

    def __init__(self, V: set[int] = None, E: set[tuple[int, int]] = None) -> None:
        """Initialize the edge set."""
        self._V = set() if V is None else V
        self._E = set() if E is None else E

    def __len__(self) -> int:
        """Return the number of vertices in the graph."""
        return len(self._V)

    def __iter__(self) -> Iterator[int]:
        """Iterate over all vertices in the graph."""
        return iter(self._V)

    def add_vertex(self, v: int) -> None:
        """Add vertex v to the graph."""
        self._V.add(v)

    def remove_vertex(self, v: int) -> None:
        """
        Remove vertex v from the graph.
        Remove all edges containing v.
        Raises a KeyError if v is not in the graph.
        """
        if v not in self._V:
            raise KeyError(f"Vertex {v} not in graph. Could not be removed.")

        self._V.remove(v)
        self._E = {e for e in self._E if v not in e}

    def add_edge(self, e: tuple[int, int]) -> None:
        """Add edge e to the graph."""
        self._E.add(e)

    def remove_edge(self, e: tuple[int, int]) -> None:
        """Remove edge e from the graph."""
        if e not in self._E:
            raise KeyError(f"Edge {e} not in graph. Could not be removed.")

        self._E.remove(e)

    def _neighbors(self, v: int) -> Iterator[int]:
        """Return an iterable of neighbors of vertex v."""
        for src, dest in self._E:
            if src == v:
                yield dest


class Graph_AS:
    """An adjacency set digraph."""

    def __init__(self, V: set[int] = None, E: set[tuple[int, int]] = None) -> None:
        """Initialize the adjacency set."""
        self._V = set() if V is None else V
        self._adj: dict[int, set[int]] = dict()
        for e in E:
            self.add_edge(e)

    def __len__(self) -> int:
        """Return the number of vertices in the graph."""
        return len(self._V)

    def __iter__(self) -> Iterator[int]:
        """Iterate over all vertices in the graph."""
        return iter(self._V)

    def add_vertex(self, v: int) -> None:
        """Add vertex v to the graph."""
        self._V.add(v)

    def remove_vertex(self, v: int) -> None:
        """
        Remove vertex v from the graph.
        Remove all edges containing v.
        Raises a KeyError if v is not in the graph.
        """
        if v not in self._V:
            raise KeyError(f"Vertex {v} not in graph. Could not be removed.")

        self._V.remove(v)

        if v in self._adj:
            self._adj.pop(v)
        for src in self._adj:
            if v in self._adj[src]:
                self._adj[src].remove(v)

    def add_edge(self, e: tuple[int, int]) -> None:
        """Add edge e to the graph."""
        src, target = e
        if src not in self._adj:
            self._adj[src] = set()

        self._adj[src].add(target)

    def remove_edge(self, e: tuple[int, int]) -> None:
        """Remove edge e from the graph."""
        src, target = e
        if (src not in self._adj) or (target not in self._adj[src]):
            raise KeyError(f"Edge {e} not in graph. Could not be removed.")

        self._adj[src].remove(target)

    def _neighbors(self, v: int) -> Iterator[int]:
        """Return an iterable of neighbors of vertex v."""
        return iter(self._adj[v])
