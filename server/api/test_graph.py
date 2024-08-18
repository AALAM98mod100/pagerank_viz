from django.test import TestCase
from .models import Graph, Node, Edge


class GraphModelTest(TestCase):
    def setUp(self):
        self.graph = Graph.objects.create(name="Test Graph")
        self.node1 = self.graph.add_node(name="Node 1")
        self.node2 = self.graph.add_node(name="Node 2")
        self.node3 = self.graph.add_node(name="Node 3")
        self.edge1 = self.graph.add_edge(from_node=self.node1, to_node=self.node2)
        self.edge2 = self.graph.add_edge(from_node=self.node2, to_node=self.node3)

    def test_graph_creation(self):
        self.assertEqual(self.graph.name, "Test Graph")

    def test_add_node(self):
        self.assertEqual(self.graph.nodes.count(), 3)
        self.assertIn(self.node1, self.graph.nodes)
        self.assertIn(self.node2, self.graph.nodes)
        self.assertIn(self.node3, self.graph.nodes)

    def test_add_edge(self):
        self.assertEqual(self.graph.edges.count(), 2)
        self.assertIn(self.edge1, self.graph.edges)
        self.assertIn(self.edge2, self.graph.edges)

    def test_serialize(self):
        serialized_graph = self.graph.serialize()
        self.assertEqual(serialized_graph["id"], self.graph.id)
        self.assertEqual(len(serialized_graph["nodes"]), 3)
        self.assertEqual(len(serialized_graph["edges"]), 2)

    def test_serialize_short(self):
        serialized_graph_short = self.graph.serialize_short()
        self.assertEqual(serialized_graph_short["id"], self.graph.id)
        self.assertEqual(serialized_graph_short["name"], self.graph.name)

    def test_calculate_pagerank(self):
        self.graph.calculate_pagerank()
        for node in self.graph.nodes:
            self.assertGreaterEqual(node.pagerank_value, 0)
            self.assertLessEqual(node.pagerank_value, 1)
        total_pagerank = sum(node.pagerank_value for node in self.graph.nodes)
        self.assertAlmostEqual(total_pagerank, 1.0, places=5)
