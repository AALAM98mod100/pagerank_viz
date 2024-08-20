from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_graph/", views.create_graph, name="create_graph"),
    path("get_graph/<int:graph_id>", views.get_graph, name="get_graph"),
    path("add_node/<int:graph_id>", views.add_node, name="add_node"),
    path("add_edge/<int:graph_id>", views.add_edge, name="add_edge"),
    path("get_neighbors/<int:node_id>", views.get_neighbors, name="get_neighbors"),
    path("calculate_pagerank/<int:graph_id>", views.calculate_pagerank, name="calculate_pagerank"),
]
