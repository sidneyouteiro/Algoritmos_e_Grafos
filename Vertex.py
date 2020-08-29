class Vertex:
    def __init__(self, label):
        self.label = label
        self.nbhood = dict()

    def add_neighbor(self, v):
        if v.label in self.nbhood.keys():
            return f'{v.label} is already a neighbor of {self.label}'
        self.nbhood[v.label] = v

    def degree(self):
        return len(self.nbhood)

    def __str__(self):
        s = f'\nId do vertice = {self.label}. Vizinhança: '
        for v in self.nbhood.keys():
            s += f'{v} '
        s += '\n'
        return s
