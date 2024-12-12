from queue import Queue
from typing import Iterator


class Graph:
    """A graph represented by an adjacency set."""

    def __init__(self, V: set | None = None, E: set | None = None) -> None:
        self.V = set()
        self.adj = dict()

        if V:
            for v in V:
                self.add_vertex(v)

        if E:
            for u, v in E:
                self.add_edge(u, v)

    def add_vertex(self, v) -> None:
        self.V.add(v)

    def remove_vertex(self, v) -> None:
        self.V.remove(v)

    def add_edge(self, u, v) -> None:
        if u not in self.adj:
            self.adj[u] = set()
        self.adj[u].add(v)

        if v not in self.adj:
            self.adj[v] = set()
        self.adj[v].add(u)

    def remove_edge(self, u, v) -> None:
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def get_neighbors(self, v) -> Iterator:
        yield from self.adj[v]

    def is_connected(self, u, v, visited: set = None) -> bool:
        visited = visited if visited else set()
        if u in visited:
            return False
        visited.add(u)

        if u == v:
            return True

        for neighbor in self.get_neighbors(u):
            if self.is_connected(neighbor, v):
                return True
        return False

    def dfs(self, v) -> dict:
        tree = {}
        to_visit = [(None, v)]

        while to_visit:
            src, dest = to_visit.pop()

            if dest in tree:
                continue
            tree[dest] = src

            for neighbor in self.get_neighbors(dest):
                to_visit.append((dest, neighbor))

        return tree

    def recursive_dfs(self, v, tree: dict | None = None) -> dict:
        tree = {v: None} if not tree else tree

        for neighbor in self.get_neighbors(v):
            if neighbor not in tree:
                tree[neighbor] = v
                self.recursive_dfs(neighbor, tree)

        return tree

    def bfs(self, v) -> dict:
        tree = {}
        to_visit = Queue()
        to_visit.put((None, v))

        while not to_visit.empty():
            src, dest = to_visit.get()

            if dest in tree:
                continue
            tree[dest] = src

            for neighbor in self.get_neighbors(dest):
                to_visit.put(dest, neighbor)

        return tree
