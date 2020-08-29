from Vertex import Vertex
from Graph import Graph


def test_del_vertex():
    g = Graph()
    g.add_vertex('1')
    print(g)
    g.del_vertex('1')
    print(g)

