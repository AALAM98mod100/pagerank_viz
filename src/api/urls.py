from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_edge/<int:graph_id>", views.add_edge),
    path("add_node/<int:graph_id>", views.add_node),
    path("create_graph/", views.create_graph, name="create_graph"),
    path("calculate_pagerank/<int:graph_id>", views.calculate_pagerank),
    path("get_graph/<int:graph_id>", views.get_graph, name="get_graph"),
    path("remove_node/", views.remove_node),
    path("remove_edge/", views.remove_edge),
    path("get_edges/", views.get_edges),
]
