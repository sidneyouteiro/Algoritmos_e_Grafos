from Vertex import Vertex
from Graph import Graph


def test_del_vertex():
    g = Graph()
    g.add_vertex('1')
    print(g)
    g.del_vertex('1')
    print(g)

def test_compact():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(3)
    g.add_edge(1, 3)
    print(g)
    g.compact()
    print(g)

test_compact()
