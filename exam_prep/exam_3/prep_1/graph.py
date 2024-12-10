from queue import Queue


class EdgeSetGraph:
    def __init__(self, V=None, E=None):
        self.V = set()
        self.E = set()

        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for u, v in E:
                self.add_edge(u, v)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, u, v):
        self.E.add((u, v))

    def remove_edge(self, u, v):
        self.E.remove((u, v))

    def neighbors(self, v):
        for u, w in self.E:
            if u == v:
                yield w


class UndirectedEdgeSetGraph(EdgeSetGraph):
    def add_edge(self, u, v):
        self.E.add(frozenset((u, v)))

    def remove_edge(self, u, v):
        self.E.remove(frozenset((u, v)))

    def neighbors(self, v):
        for u, w in self.E:
            if u == v:
                yield w
            elif w == v:
                yield u


class AdjacencySetGraph:
    def __init__(self, V=None, E=None):
        self.V = set()
        if V:
            for v in V:
                self.add_vertex(v)

        self.adj = dict()
        if E:
            for u, v in E:
                self.add_edge(u, v)

    def add_vertex(self, v):
        self.V.add(v)

    def remvoe_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = set()
        self.adj[u].add(v)

    def remove_edge(self, u, v):
        self.adj[u].remove(v)

    def neighbors(self, v):
        return self.adj.get(v, tuple())

    def is_connected(self, u, v, visited=None):
        if u == v:
            return True

        if not visited:
            visited = set()

        if u in visited:
            return False
        else:
            visited.add(u)

        for neighbor in self.neighbors(u):
            if self.is_connnected(neighbor, v, visited):
                return True
        return False

    def depth_first_search(self, v):
        tree = dict()  # Will map node -> parent.
        to_visit = [(None, v)]  # tuples of parent -> node

        while to_visit:
            parent, node = to_visit.pop()
            if node in tree:
                continue

            tree[node] = parent
            for neighbor in self.neighbors(node):
                to_visit.append(node, neighbor)

        return tree

    def breadth_first_search(self, v):
        tree = {}  # Maps node -> parent

        to_visit = Queue()  # tuples of (parent, node)
        to_visit.put((None, v))

        while not to_visit.empty():
            parent, node = to_visit.get()

            if node in tree:
                continue

            tree[node] = parent
            for neighbor in self.neighbors(node):
                to_visit.put((node, neighbor))

        return tree
