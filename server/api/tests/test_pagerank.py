import unittest
from pagerank import PageRank


class TestPageRank(unittest.TestCase):
    def test_initialization(self):
        graph = {"A": ["B"], "B": ["A"]}
        pr = PageRank(graph)
        self.assertEqual(pr.graph, graph)
        self.assertEqual(pr.damping_factor, 0.85)
        self.assertEqual(pr.max_iterations, 100)
        self.assertEqual(pr.tolerance, 1e-6)

    def test_run_simple_graph(self):
        graph = {"A": ["B"], "B": ["A"]}
        pr = PageRank(graph)
        result = pr.run()
        self.assertAlmostEqual(result["A"], 0.5, places=2)
        self.assertAlmostEqual(result["B"], 0.5, places=2)

    def test_run_disconnected_graph(self):
        graph = {"A": [], "B": []}
        pr = PageRank(graph)
        result = pr.run()
        self.assertAlmostEqual(result["A"], 0.5, places=2)
        self.assertAlmostEqual(result["B"], 0.5, places=2)

    def test_run_complex_graph(self):
        graph = {"A": ["B", "C"], "B": ["C"], "C": ["A"], "D": ["C"]}
        pr = PageRank(graph)
        result = pr.run()
        self.assertAlmostEqual(result["A"], 0.33, places=2)
        self.assertAlmostEqual(result["B"], 0.18, places=2)
        self.assertAlmostEqual(result["C"], 0.33, places=2)
        self.assertAlmostEqual(result["D"], 0.18, places=2)


if __name__ == "__main__":
    unittest.main()
