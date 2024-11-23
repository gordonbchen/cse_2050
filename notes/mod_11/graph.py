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


class AdjacencySet:
    def __init__(self, V=None, E=None):
        self._V = set()
        self._neighbors = dict()

        if V is not None:
            for v in V:
                self.add_vertex(v)

        if E is not None:
            for u, v in E:
                self.add_edge(u, v)

    def add_vertex(self, v):
        self._V.add(v)

    def remove_vertex(self, v):
        self._V.remove(v)

    def add_edge(self, u, v):
        if u not in self._neighbors:
            self._neighbors[u] = set()
        self._neighbors[u].add(v)

    def remove_edge(self, u, v):
        self._neighbors[u].remove(v)
        if len(self._neighbors[u]) == 0:
            self._neighbors.pop(u)

    def __iter__(self):
        return self._V

    def get_neighbors(self, v):
        return self._neighbors[v]

    def connected(self, v, target, visited=None):
        if visited is None:
            visited = set()

        if v in visited:
            return False

        if v == target:
            return True

        visited.add(v)

        for neighbor in self.get_neighbors(v):
            if self.connected(neighbor, target, visited):
                return True
        return False

    def depth_first_search_iter(self, v):
        tree = {}
        to_visit = [(None, v)]

        while len(to_visit) > 0:
            src, dest = to_visit.pop()
            if dest in tree:
                continue

            tree[dest] = src
            for neighbor in self.get_neighbors(dest):
                to_visit.append((dest, neighbor))

        return tree

    def breadth_first_search_iter(self, v):
        tree = {}
        to_visit = [(None, v)]

        while len(to_visit) > 0:
            src, dest = to_visit.pop(0)
            if dest in tree:
                continue

            tree[dest] = src
            for neighbor in self.get_neighbors(dest):
                to_visit.append((dest, neighbor))

        return tree


if __name__ == "__main__":
    V = {1, 2, 3, 4}
    E = {(1, 2), (3, 4), (4, 2), (3, 1)}

    di_graph = DirectedEdgeSetGraph(V, E)
    print(list(di_graph.get_neighbors(1)))

    un_digraph = UndirectedEdgeSetGraph(V, E)
    print(list(un_digraph.get_neighbors(1)))

    adj_graph = AdjacencySet(V, E)
    print(adj_graph.get_neighbors(1))
