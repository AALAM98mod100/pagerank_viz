import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from api.models import Graph, Node, Edge

graph = Graph.objects.get(id=1)
graph.calculate_pagerank()
