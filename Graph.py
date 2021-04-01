from Vertex import Vertex
from copy import deepcopy

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
    
    def del_edge(self,label1,label2):
        v1 = self.vertex_set[label1]
        v2 = self.vertex_set[label2]

        v1.del_neighbor(v2)
        v2.del_neighbor(v1)

    def add_edge(self, label1, label2):
        v1 = self.vertex_set[label1]
        v2 = self.vertex_set[label2]

        v1.add_neighbor(v2)
        v2.add_neighbor(v1)

    def del_vertex(self, label):
        v = self.vertex_set[label]

        for u in v.nbhood.values():
            u.nbhood.pop(label, None)

        self.vertex_set.pop(label, None)

    def change_label(self, old_label, new_label):
        for v in self.vertex_set.values():
            if old_label in v.nbhood.keys():
                v.nbhood[new_label] = v.nbhood[old_label]
                v.nbhood[new_label].label = new_label
                del v.nbhood[old_label]

        self.vertex_set[new_label] = self.vertex_set[old_label]
        self.vertex_set[new_label].label = new_label
        del self.vertex_set[old_label]

    def _compact(self):
        old_labels = list(self.vertex_set.keys())

        for i in range(len(old_labels)):
            self.change_label(old_labels[i], i)

    def compact(self):
        n = len(self.vertex_set)
        present = [0] * (n+1)
        stranges = []

        # present marks with 1 those who are present
        # stranges has vertexes whose labels > n
        for v in self.vertex_set.values():
            if v.label <= n:
                present[v.label] = 1
            else:
                stranges += [v]

        # now present has the matching empty pair
        i = 0
        pairs = 0
        while pairs < len(stranges):
            if present[i] == 0:
                present[pairs] = i
                pairs += 1
            i += 1

        for i in range(len(stranges)):
            old_label = stranges[i].label
            stranges[i].label = present[i]

            for v in self.vertex_set.values():
                if old_label in v.nbhood.keys():
                    del v.nbhood[old_label]
                    v.nbhood[stranges[i].label] = stranges[i]

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

    def BFS(self, root):
        visited = [False] * ( max(self.vertex_set.keys()) + 1 )
        q = []

        q += [root]
        visited[root] = True

        while len(q) > 0:
            v = self.vertex_set[q.pop(0)]
            
            for u in v.nbhood.values():
                if not visited[u.label]:
                    visited[u.label] = True
                    q += [u.label]

        return [label for label in range(len(visited)) if visited[label]]

    def is_connected(self,root):
        if self.is_undirected():
            if len(self.BFS(root)) == len(self.vertex_set):
                return True

        return False

    def __str__(self):
        s = '\n\n' + f'Grafo, grau máximo {self.max_degree()}' + '\n'

        if self.is_undirected():
            s += 'Não direcionado\n'
        else:
            s += 'Direcionado\n'

        for v in self.vertex_set.values():
            s += v.__str__()

        return s

      
        
    def is_copwin(self):
        if not self.is_connected(list(self.vertex_set.keys())[0]): # verifica se o grafo é desconexo
            return False, 'O grafo é desconexo, portanto não é copwin'
        # tenho um array de vertices deletados e um auxiliar
        delV = ''
        auxDelV = []
        #intera enquanto o auxiliar for receber vertices a cada interação 
        while (auxDelV != delV): 
            delV = list(auxDelV)
            for v in list(self.vertex_set.values()):# vai em cada vertice do grafo
                if v.label in auxDelV:#caso esteja no auxDelV ignora
                    continue
                #pega a vizinhança fechada exceto os vertices na lista de deletados auxiliar
                vizinhancaFechada = list(set(list(v.nbhood.keys()))-set(auxDelV))
                vizinhancaFechada.append(v.label)
                for v2 in list(v.nbhood.values()): #pega cada vizinho do vertice v
                    if v2.label in auxDelV:#caso esteja no auxDelV ignora
                        continue
                    #pega a vizinhança fechada exceto os vertices na lista de deletados auxiliar
                    vizinhancaFechada2 = list(set(list(v2.nbhood.keys()))-set(auxDelV))
                    vizinhancaFechada2.append(v2.label)
                    #caso a vizinhança fechada de um vizinho do vertice v seja um subconjunto
                    #da vizinhança fechada de v, então ele pode ser removido sem alterar o fato
                    #do grafo ser ou não ser copwin
                    if (all(x in vizinhancaFechada for x in vizinhancaFechada2)):
                        auxDelV.append(v2.label)
        for i in auxDelV:
            self.del_vertex(i)
        #caso tenha restado apenas um vertice, ou seja um C3 ou C2 então é copwin
        if len(self.vertex_set)<=3:
            return True,''
        else:
            return False,'O grafo possui um ciclo com 4 ou mais vertices, portanto não é copwin'


    global cor
    
    def isBipartido(self):
        global cor
        cor ={}
        for v in list(self.vertex_set.keys()):

            cor[v]=-1
        
        for v in list(self.vertex_set.keys()):
            if (cor[v]==-1):
                if(not self.defineCor(v,0)):
                    return False, None
        conjuntos={}
        conjuntos[0]=[]
        conjuntos[1]=[]
        for i in cor:
            if cor [i] == 1:
                conjuntos[1].append(i)
            else:
                conjuntos[0].append(i)
        return True, conjuntos

    def defineCor(self,vertex,c):
        global cor
        cor[vertex]=c
        for u in list(self.vertex_set[vertex].nbhood.keys()):
            if cor[u] == -1:
                if self.defineCor(u,1-c) == False:
                    return False
                else:
                    if cor[u] == c:
                        return False
        return True
    
    def recursivoDFS(self,vertex,emparelhado,visitado,result):
        for v in result[0]:

            if v in list(self.vertex_set[vertex].nbhood.keys()) and visitado[v-1] == False:
                visitado[v-1]=True
                if emparelhado[v-1] == -1 or self.recursivoDFS(emparelhado[v-1],emparelhado,visitado,result):
                    emparelhado[v-1]=vertex
                    return True
        return False

    def EmparelhamentoMaximo(self):
        b, result = self.isBipartido()
        if not b:
            return 'Esse grafo não é bipartido'
        
        emparelhado = [-1] * (len(result[0])+len(result[1]))
        cont = 0
        for i in result[1]:
            visitado = [False] * (len(result[0])+len(result[1]))
            
            if self.recursivoDFS(i,emparelhado,visitado,result):
                cont = cont+1
        for i,j in enumerate(emparelhado):
            if j != -1:
                print('match',i,j)
        return 'O emparelhamento maximo é '+ str(cont)