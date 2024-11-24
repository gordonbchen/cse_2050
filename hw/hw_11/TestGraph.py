import unittest

from typing import Any

from Graph import Graph, AdjacencySetGraph, EdgeSetGraph


class GraphTestFactory:
    """Tests for the graph ADT."""

    graph_class: type[Graph]

    def check_vertex_exists(self, v: Any, graph: Graph) -> bool:
        """Return True if the vertex exists. ADT implementation defined."""
        raise NotImplementedError()

    def check_edge_exists(self, v1: Any, v2: Any, graph: Graph) -> bool:
        """Return True if the edge exists. ADT implemenation defined."""
        raise NotImplementedError()

    def test_create_empty_graph(self) -> None:
        """Test creating an empty graph and adding vertices and edges."""
        graph = self.graph_class()

        # 0---1
        # | /
        # 2---3
        V = {0, 1, 2, 3}
        E = {(0, 1), (0, 2), (1, 2), (2, 3)}

        for v in V:
            graph.add_vertex(v)
        for e in E:
            graph.add_edge(e)

        for v in V:
            self.assertTrue(self.check_vertex_exists(v, graph))
        for e in E:
            self.assertTrue(self.check_edge_exists(e[0], e[1], graph))

    def test_create_graph(self) -> None:
        """Test creating a graph with given vertices and edges."""
        # 0---1
        # | /
        # 2---3
        V = {0, 1, 2, 3}
        E = {(0, 1), (0, 2), (1, 2), (2, 3)}
        graph = self.graph_class(V, E)

        for v in V:
            self.assertTrue(self.check_vertex_exists(v, graph))
        for e in E:
            self.assertTrue(self.check_edge_exists(e[0], e[1], graph))

    def get_cyclic_graph(self) -> Graph:
        """Create and return a cyclic graph."""
        # 0---1         6---7
        # | /             \ |
        # 2---3---5         8
        # |       |
        # 4--------
        V = {0, 1, 2, 3, 4, 5, 6, 7, 8}
        E = {(0, 1), (0, 2), (1, 2), (2, 3), (3, 5), (2, 4), (5, 4), (6, 7), (6, 8), (7, 8)}
        graph = self.graph_class(V, E)
        return graph

    def test_is_connected_simple(self) -> None:
        """Test graph connections in a simple graph."""
        # 0---1         6---7
        # |
        # 2---3---5
        # |
        # 4
        V = {0, 1, 2, 3, 4, 5, 6, 7}
        E = {(0, 1), (0, 2), (2, 3), (3, 5), (2, 4), (6, 7)}
        graph = self.graph_class(V, E)

        for i in range(6):
            for j in range(6):
                self.assertTrue(graph.is_connected(i, j))

            for j in (6, 7):
                self.assertFalse(graph.is_connected(i, j))

        for i in (6, 7):
            for j in (6, 7):
                self.assertTrue(graph.is_connected(i, j))

            for j in range(6):
                self.assertFalse(graph.is_connected(i, j))

    def test_is_connected_cycle(self) -> None:
        """Test graph connections in a cyclic graph."""
        graph = self.get_cyclic_graph()

        for i in range(6):
            for j in range(6):
                self.assertTrue(graph.is_connected(i, j))

            for j in range(6, 9):
                self.assertFalse(graph.is_connected(i, j))

        for i in range(6, 9):
            for j in range(6, 9):
                self.assertTrue(graph.is_connected(i, j))

            for j in range(6):
                self.assertFalse(graph.is_connected(i, j))

    def test_bfs(self) -> None:
        """Test getting a breadth-first search tree."""
        graph = self.get_cyclic_graph()
        # 0---1         6---7
        # | /             \ |
        # 2---3---5         8
        # |       |
        # 4--------

        # Test dists from 0.
        dists_from_0_expected = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3}

        bfs_tree_0 = graph.bfs(0)
        dists_from_0_calculated = self.get_dists_from_bfs_tree(bfs_tree_0, 0)

        self.assertEqual(dists_from_0_expected, dists_from_0_calculated)

        # Tests dists from 6.
        dists_from_6_expected = {6: 0, 7: 1, 8: 1}

        bfs_tree_6 = graph.bfs(6)
        dists_from_6_calculated = self.get_dists_from_bfs_tree(bfs_tree_6, 6)

        self.assertEqual(dists_from_6_expected, dists_from_6_calculated)

    def get_dists_from_bfs_tree(self, bfs_tree: dict, target_vertex: Any) -> dict:
        """
        Find the distance from each vertex in the bfs tree to the target vertex.
        Returns a dictionary mapping vertex: dist to target vertex.
        """
        dists = {}
        for v in bfs_tree:
            path_length = 0
            curr_v = v
            while curr_v != target_vertex:
                path_length += 1
                curr_v = bfs_tree[curr_v]

            dists[v] = path_length
        return dists

    def test_count_trees(self) -> None:
        """Test counting separated trees in the graph."""
        graph = self.get_cyclic_graph()
        # 0---1         6---7
        # | /             \ |
        # 2---3---5         8
        # |       |
        # 4--------

        trees, n_trees = graph.count_trees()
        self.assertEqual(n_trees, len(trees))
        self.assertEqual(len(trees), 2)

        for tree in trees:
            if 0 in tree:
                self.assertTrue(len(tree) == 6)
                for i in range(6):
                    self.assertTrue(i in tree)
            else:
                self.assertTrue(len(tree) == 3)
                for i in range(6, 9):
                    self.assertTrue(i in tree)

    def test_shortest_path(self) -> None:
        """Test finding the shortest path between vertices."""
        graph = self.get_cyclic_graph()
        # 0---1         6---7
        # | /             \ |
        # 2---3---5         8
        # |       |
        # 4--------

        # Check that trying to find the shortest path b/t disconnected vertices raises an error.
        for i in range(6):
            for j in range(6, 9):
                with self.assertRaises(ValueError):
                    graph.shortest_path(i, j)
                with self.assertRaises(ValueError):
                    graph.shortest_path(j, i)

        # Test shortest path from 0.
        dists_from_0_expected = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3}

        for v in range(6):
            path = graph.shortest_path(0, v)
            self.assertEqual(len(path), dists_from_0_expected[v] + 1)

            for i in range(len(path) - 1):
                v1 = path[i]
                v2 = path[i + 1]
                self.assertTrue(self.check_edge_exists(v1, v2, graph))


class TestAdjacency(GraphTestFactory, unittest.TestCase):
    """Tests for the adjacency graph."""

    def setUp(self) -> None:
        """Set the graph class."""
        self.graph_class = AdjacencySetGraph

    def check_vertex_exists(self, v: Any, graph: AdjacencySetGraph) -> bool:
        """Return True if the vertex exists."""
        return v in graph._V

    def check_edge_exists(self, v1: Any, v2: Any, graph: AdjacencySetGraph) -> bool:
        """Return True if the edge exists."""
        return v2 in graph._adj[v1]


class TestEdge(GraphTestFactory, unittest.TestCase):
    """Tests for the edge graph."""

    def setUp(self) -> None:
        """Set the graph class."""
        self.graph_class = EdgeSetGraph

    def check_vertex_exists(self, v: Any, graph: EdgeSetGraph) -> bool:
        """Return True if the vertex exists."""
        return v in graph._V

    def check_edge_exists(self, v1: Any, v2: Any, graph: EdgeSetGraph) -> bool:
        """Return True if the edge exists."""
        return frozenset((v1, v2)) in graph._E


if __name__ == "__main__":
    unittest.main()
