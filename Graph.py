from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertex_set = dict()

    def add_vertex(self, label):
        if label not in self.vertex_set.keys():
            v = Vertex(label)
            self.vertex_set[label] = v
        else:
            return f'{label} already exists in this graph.'

    def add_arc(self, label1, label2):
        v1 = self.vertex_set[label1]
        v2 = self.vertex_set[label2]

        v1.add_neighbor(v2)

    def add_edge(self, label1, label2):
        v1 = self.vertex_set[label1]
        v2 = self.vertex_set[label2]

        v1.add_neighbor(v2)
        v2.add_neighbor(v1)

    def del_vertex():
        # TODO
        pass

    def compact():
        # TODO
        pass

    def max_degree(self):
        max_deg = 0

        for v in self.vertex_set.values():
            max_deg = max(max_deg, len(v.nbhood))

        return max_deg

    def is_undirected(self):
        for v in self.vertex_set.values():
            for u in v.nbhood.values():
                if v not in u.nbhood.values():
                    return False
        return True

    def subjacent(self):
        subj = Graph()

        for v in self.vertex_set.keys():
            subj.add_vertex(v)

        for v in self.vertex_set.values():
            for u in v.nbhood.values():
                v_subj = subj.vertex_set[v.label]
                u_subj = subj.vertex_set[u.label]

                v_subj.add_neighbor(u_subj)
                u_subj.add_neighbor(v_subj)

        return subj

    def is_connected():
        # TODO
        pass

    def BFS():
        # TODO
        pass

    def __str__(self):
        s = '\n\n' + f'Grafo, grau máximo {self.max_degree()}' + '\n'

        if self.is_undirected():
            s += 'Não direcionado\n'
        else:
            s += 'Direcionado\n'

        for v in self.vertex_set.values():
            s += v.__str__()

        return s
