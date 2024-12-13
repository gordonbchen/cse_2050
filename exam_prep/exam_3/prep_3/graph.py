from typing import Any
from queue import Queue


class Graph:
    def __init__(self, V: set | None = None, E: set | None = None) -> None:
        self.V = set()
        self.adj = dict()

        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for u, v in E:
                self.add_edge(u, v)

    def add_vertex(self, v: Any) -> None:
        self.V.add(v)

    def remove_vertex(self, v: Any) -> None:
        self.V.remove(v)

    def add_edge(self, u: Any, v: Any) -> None:
        if u not in self.adj:
            self.adj[u] = set()
        self.adj[u].add(v)

        if v not in self.adj:
            self.adj[v] = set()
        self.adj[v].add(u)

    def remove_edge(self, u: Any, v: Any) -> None:
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def get_neighbors(self, v: Any) -> set:
        return self.adj.get(v, default=set())

    def is_connected(self, u: Any, v: Any) -> bool:
        return self._is_connected(u, v, set())

    def _is_connected(self, u: Any, v: Any, visited: set) -> bool:
        if u == v:
            return True

        if u in visited:
            return False
        visited.add(u)

        return any(self._is_connected(neighbor, v, visited) for neighbor in self.get_neighbors(u))

    def recursive_dfs(self, v: Any) -> dict:
        tree = {v: None}
        self._recursive_dfs(v, tree)
        return tree

    def _recursive_dfs(self, v: Any, tree: dict) -> None:
        for neighbor in self.get_neighbors(v):
            if neighbor not in tree:
                tree[neighbor] = v
                self._recursive_dfs(neighbor, tree)

    def dfs(self, v: Any) -> dict:
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

    def bfs(self, v: Any) -> dict:
        tree = {}

        to_visit = Queue()
        to_visit.put((None, v))

        while not to_visit.empty():
            src, dest = to_visit.get()

            if dest in tree:
                continue
            tree[dest] = src

            for neighbor in self.get_neighbors(dest):
                to_visit.put((dest, neighbor))

        return tree
