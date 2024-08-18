import logging
from django.db import models
from django.db.models import Q
from django.utils.functional import cached_property

logger = logging.getLogger(__name__)


class GraphQuerySet(models.QuerySet):
    pass


class GraphManager(models.Manager.from_queryset(GraphQuerySet)):
    def get_by_id(self, _id):
        try:
            return self.get(id=_id)
        except Graph.DoesNotExist:
            logger.error("Graph with id: %d does not exist", _id)


class Graph(models.Model):
    name = models.CharField(max_length=100)

    objects = GraphManager()

    def __str__(self):
        return self.name

    def add_node(self, name):
        return Node.objects.create(name=name, graph=self)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.add_node("Node 1")
    #     super().save(*args, **kwargs)

    def add_edge(self, from_node, to_node):
        return Edge.objects.create(from_node=from_node, to_node=to_node)

    @property
    def nodes(self):
        return Node.objects.filter(graph=self)

    @property
    def edges(self):
        return Edge.objects.filter(
            Q(from_node__graph=self) | Q(to_node__graph=self)
        ).distinct()

    def serialize(self):
        """Serialize the graph getting all the nodes and returning a dictionary with the graph and its nodes.

        Returns
        -------
            dict
        """
        return {
            "id": self.id,
            "nodes": [node.serialize() for node in self.nodes],
            "edges": [edge.serialize() for edge in self.edges],
        }

    def serialize_short(self):
        """Returns a short serialization of graph containing only name and id dict

        Returns
        -------
            dict
        """
        return {
            "id": self.id,
            "name": self.name,
        }

    def get_neighbors(self, node):
        return Node.objects.filter(
            Q(from_node__in=node.edges) | Q(to_node__in=node.edges)
        ).exclude(id=node.id)

    def calculate_pagerank(self, d=0.85, iterations=100):
        nodes = self.nodes
        n_nodes = len(nodes)
        page_rank = {node: 1 / n_nodes for node in nodes}
        for _ in range(iterations):
            new_page_rank = {}
            for node in nodes:
                new_page_rank[node] = (1 - d) + d * sum(
                    page_rank[neighbor] / len(self.get_neighbors(neighbor))
                    for neighbor in self.get_neighbors(node)
                )

            # Normalize the new PageRank values
            total_rank = sum(new_page_rank.values())
            for node in new_page_rank:
                new_page_rank[node] /= total_rank

            page_rank = new_page_rank

        nodes_to_update = []
        for node in nodes:
            node.pagerank_value = page_rank[node]
            nodes_to_update.append(node)
        Node.objects.bulk_update(nodes_to_update, fields=["pagerank_value"])


class Node(models.Model):
    name = models.CharField(max_length=100)
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    pagerank_value = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    @property
    def edges(self):
        return Edge.objects.filter(from_node=self) | Edge.objects.filter(to_node=self)

    def serialize(self):
        """Serialize the node getting all the edges and returning a dictionary with the node and its edges.

        Returns
        -------
            dict
        """
        return {
            "id": self.id,
            "label": self.name,
            "title": f"This is {self.name}",
            "value": self.pagerank_value,
            "edges": [
                {"from": edge.from_node.id, "to": edge.to_node.id}
                for edge in self.edges
            ],
        }


class Edge(models.Model):
    from_node = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name="from_node"
    )
    to_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="to_node")

    def __str__(self):
        return f"{self.from_node} -> {self.to_node}"

    def serialize(self):
        # [
        #         {"from": edge.from_node.id, "to": edge.to_node.id}
        #         for node in self.nodes
        #         for edge in node.edges
        #     ],
        return {
            "from": self.from_node.id,
            "to": self.to_node.id,
        }
