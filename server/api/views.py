import time
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Graph


@api_view(["GET"])
def home(request):
    try:
        all_graphs = Graph.objects.all()
        list_of_graphs = [graph.serialize_short() for graph in all_graphs]
        return JsonResponse(list_of_graphs, safe=False)
    except Exception as e:
        raise e


@api_view(["GET"])
def get_graph(request, graph_id):
    graph = Graph.objects.get_by_id(graph_id)
    graph_data: Graph = graph.serialize()
    # return test reponse for vis-network
    # graph_data = {
    #     "nodes": [
    #         {"id": 1, "label": "Node 1"},
    #         {"id": 2, "label": "Node 2"},
    #         {"id": 3, "label": "Node 3"},
    #         {"id": 4, "label": "Node 4"},
    #         {"id": 5, "label": "Node 5"},
    #     ],
    #     "edges": [
    #         {"from": 1, "to": 2},
    #         {"from": 1, "to": 3},
    #         {"from": 2, "to": 4},
    #         {"from": 2, "to": 5},
    #         {"from": 3, "to": 3},
    #     ],
    # }
    return JsonResponse(graph_data)


def calculate_pagerank(request, graph_id):
    graph: Graph = Graph.objects.get_by_id(graph_id)
    try:
        now = time.time()
        graph.calculate_pagerank()
        t = time.time() - now
        graph.refresh_from_db()
        response = graph.serialize()
        response.update({"time": t})
        return JsonResponse(response)
    except Exception as e:
        print(e)


@api_view(["POST"])
def create_graph(request):
    from api.models import Graph

    name = request.data["name"]
    graph = Graph.objects.create(name=name)
    response = {
        "graph": graph.serialize_short(),
        "graphs": [g.serialize_short() for g in Graph.objects.all()],
    }
    return JsonResponse(response, safe=False)


@api_view(["GET"])
def get_neighbors(request, node_id):
    from api.models import Node

    try:
        node = Node.objects.get(id=node_id)
        neighbors = node.neighbors
        neighbors = [n.serialize() for n in neighbors]
    except Node.DoesNotExist:
        neighbors = ["Something went wrong"]
    return JsonResponse(neighbors, safe=False)


@api_view(["GET"])
def get_edges(request):
    return JsonResponse(graph.graph)


@api_view(["POST"])
def add_node(request, graph_id):
    graph: Graph = Graph.objects.get_by_id(graph_id)
    node_name = request.data["name"]
    graph.add_node(node_name)
    return JsonResponse(graph.serialize())


@api_view(["POST"])
def add_edge(request, graph_id):
    graph: Graph = Graph.objects.get_by_id(graph_id)
    from_node = request.data["nodeOne"]
    from_node = graph.nodes.get(name=from_node)
    to_node = request.data["nodeTwo"]
    to_node = graph.nodes.get(name=to_node)
    graph.add_edge(from_node, to_node)
    return JsonResponse(graph.serialize())


@api_view(["POST"])
def remove_node(request):
    node_name = request.data["node"]
    graph.remove_node(node_name)
    return JsonResponse({"status": "Node removed"})


@api_view(["POST"])
def remove_edge(request):
    from_node = request.data["from"]
    to_node = request.data["to"]
    graph.remove_edge(from_node, to_node)
    return JsonResponse({"status": "Edge removed"})
