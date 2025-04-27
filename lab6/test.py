import unittest

from main import client_server_latency

class TestClientServerLatency(unittest.TestCase):

    def test_example_1(self):
        NM = (6, 6)
        clients = (1, 2, 6)
        links = (
            (1, 3, 10),
            (3, 4, 80),
            (4, 5, 50),
            (5, 6, 20),
            (2, 3, 40),
            (2, 4, 100),
        )
        expected = 100
        result = client_server_latency(NM, clients, *links)
        self.assertEqual(result, expected)

    def test_example_2(self):
        NM = (6, 7)
        clients = (1, 2, 6)
        links = (
            (1, 3, 10),
            (3, 4, 80),
            (4, 5, 50),
            (5, 6, 20),
            (2, 3, 40),
            (2, 4, 5),
            (1, 2, 100),
        )
        expected = 70
        result = client_server_latency(NM, clients, *links)
        self.assertEqual(result, expected)

    def test_one_node(self):
        NM = (1, 0)
        clients = (1,)
        links = ()
        expected = 0
        result = client_server_latency(NM, clients, *links)
        self.assertEqual(result, expected)

    def test_no_clients(self):
        NM = (3, 2)
        clients = ()
        links = (
            (1, 2, 5),
            (2, 3, 5),
        )
        expected = 5
        result = client_server_latency(NM, clients, *links)
        self.assertEqual(result, expected)

    def test_fully_connected(self):
        NM = (4, 6)
        clients = (1,)
        links = (
            (1, 2, 1),
            (1, 3, 5),
            (1, 4, 9),
            (2, 3, 2),
            (2, 4, 6),
            (3, 4, 3),
        )
        expected = 5
        result = client_server_latency(NM, clients, *links)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
