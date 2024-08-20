from django.test import TestCase, Client
from django.urls import reverse
from api.models import Graph


class GraphViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.graph = Graph.objects.create(name="Test Graph")
        self.node1 = self.graph.add_node("Node 1")
        self.node2 = self.graph.add_node("Node 2")
        self.graph.add_edge(self.node1, self.node2)

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_get_graph_view(self):
        response = self.client.get(reverse("get_graph", args=[self.graph.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("nodes", response.json())
        self.assertIn("edges", response.json())

    def test_calculate_pagerank_view(self):
        response = self.client.get(reverse("calculate_pagerank", args=[self.graph.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("time", response.json())

    def test_create_graph_view(self):
        response = self.client.post(
            reverse("create_graph"),
            {"name": "New Graph"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["graphs"]), 2)

    def test_get_neighbors_view(self):
        response = self.client.get(reverse("get_neighbors", args=[self.node1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_add_node_view(self):
        response = self.client.post(
            reverse("add_node", args=[self.graph.id]),
            {"name": "Node 3"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["nodes"]), 3)

    def test_add_edge_view(self):
        response = self.client.post(
            reverse("add_edge", args=[self.graph.id]),
            {"nodeOne": "Node 1", "nodeTwo": "Node 2"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["edges"]), 2)
