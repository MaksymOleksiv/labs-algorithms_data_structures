import unittest
from ..src.prim_algo import prim_mst
from ..src.csv_file_read import read_csv_file


class TestPrimMST(unittest.TestCase):

    def test_simple_graph(self):
        graph = read_csv_file("simple_graph.csv")
        self.assertEqual(prim_mst(graph), 7)

    def test_fully_connected_graph(self):
        graph = read_csv_file("fully_connected_graph.csv")
        self.assertEqual(prim_mst(graph), 3)

    def test_disconnected_graph(self):
        graph = read_csv_file("disconnected_graph.csv")
        self.assertNotEqual(prim_mst(graph), 0)

    def test_single_vertex(self):
        graph = read_csv_file("single_vertex.csv")
        self.assertEqual(prim_mst(graph), 0)

    def test_two_vertices(self):
        graph = read_csv_file("two_vertices.csv")
        self.assertEqual(prim_mst(graph), 5)


if __name__ == '__main__':
    unittest.main()
