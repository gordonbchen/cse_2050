class EdgeSetGraph:
    def __init__(self, V=None, E=None):
        self._V = set()
        self._E = set()

        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for u, v in E:
                self.add_edge(u, v)

    def add_vertex(self, v):
        self._V.add(v)

    def add_edge(self, u, v):
        raise NotImplementedError()

    def remove_edge(self, u, v):
        raise NotImplementedError()

    def get_neighbors(self, v):
        raise NotImplementedError()


class DirectedEdgeSetGraph(EdgeSetGraph):
    def add_edge(self, u, v):
        self._E.add((u, v))

    def remove_edge(self, u, v):
        self._E.remove((u, v))

    def get_neighbors(self, v):
        return (w for (u, w) in self._E if u == v)


class UndirectedEdgeSetGraph(EdgeSetGraph):
    def add_edge(self, u, v):
        self._E.add(frozenset({u, v}))

    def remove_edge(self, u, v):
        self._E.remove(frozenset({u, v}))

    def get_neighbors(self, v):
        for u, w in self._E:
            if u == v:
                yield w
            if w == v:
                yield u


if __name__ == "__main__":
    V = {1, 2, 3, 4}
    E = {(1, 2), (3, 4), (4, 2), (3, 1)}

    digraph = DirectedEdgeSetGraph(V, E)
    print(list(digraph.get_neighbors(1)))

    undigraph = UndirectedEdgeSetGraph(V, E)
    print(list(undigraph.get_neighbors(1)))
