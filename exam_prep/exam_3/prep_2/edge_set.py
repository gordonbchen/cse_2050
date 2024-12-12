from typing import Iterator


class EdgeSet:
    def __init__(self, V: set | None = None, E: set | None = None) -> None:
        self.V = set()
        self.E = set()

        if V:
            for v in V:
                self.add_vertex(V)

        if E:
            for u, v in E:
                self.add_edge(u, v)

    def add_vertex(self, v) -> None:
        self.V.add(v)

    def remove_vertex(self, v) -> None:
        self.V.remove(v)

    def add_edge(self, u, v) -> None:
        self.E.add((u, v))

    def remove_edge(self, u, v) -> None:
        self.E.remove((u, v))

    def get_neighbors(self, v) -> Iterator:
        for e in self.E:
            if e[0] == v:
                yield e[1]
