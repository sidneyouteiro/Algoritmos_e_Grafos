import os
from Vertex import Vertex
from Graph import Graph

def get_file_graph():
    graph = Graph()
    try:
        file = open(os.path.join(os.path.dirname(__file__),'myfiles','entrada.txt'), "r")
        this_line = file.readline()
        while not this_line == "" :
            this_line = this_line.replace("\n", "")
            this_line = " ".join(this_line.split())
            pieces = this_line.split(" ")
            v1 = int(pieces.pop(0))
            graph.add_vertex(v1)
            for vertex in pieces:
                if not vertex.isdigit():
                    continue
                vertex = int(vertex)
                if not graph.vertex_set.get(vertex):
                    graph.add_vertex(vertex)
                graph.add_arc(v1, vertex)
            this_line = file.readline()
        print("Arquivo lido com sucesso")
        return graph
    except Exception as e:
        print(e)
        return Graph()


def test_copwin():
    g = get_file_graph()
    result, msg = g.is_copwin()
    if result:
        print('O grafo é copwin')
    else:
        print(msg)

def test_matching():
    g = get_file_graph()
    result = g.EmparelhamentoMaximo()        
    print(result)

test_matching()
