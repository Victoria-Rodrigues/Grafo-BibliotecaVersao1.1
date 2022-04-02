from collections import defaultdict

class Fleury:
    def __init__(self,qtdVertices):
        self.V = qtdVertices
        self.grafoAuxiliar = defaultdict(list)

    def adicionarAresta(self, u, v):
        self.grafoAuxiliar[u].append(v)
        self.grafoAuxiliar[v].append(u)

    def removerAresta(self, u, v):
        for index, key in enumerate(self.grafoAuxiliar[u]):
            if key == v:
                self.grafoAuxiliar[u].pop(index)
        for index, key in enumerate(self.grafoAuxiliar[v]):
            if key == u:
                self.grafoAuxiliar[v].pop(index)


    def DFSAux(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.grafoAuxiliar[v]:
            if visited[i] == False:
                count = count + self.DFSAux(i, visited)
        return count

    def proximaArestaValida(self, u, v):
        if len(self.grafoAuxiliar[u]) == 1:
            return True
        else:
            visited = [False] * (self.V)
            count1 = self.DFSAux(u, visited)
            self.removerAresta(u, v)
            visited = [False] * (self.V)
            count2 = self.DFSAux(u, visited)
            self.adicionarAresta(u, v) 
            return False if count1 > count2 else True



    def impressaoAux(self, u):
        for v in self.grafoAuxiliar[u]:
            if self.proximaArestaValida(u, v):
                print("%d-%d " % (u+1, v+1)),
                self.removerAresta(u, v)
                self.impressaoAux(v)

    def cadeiaEuleriana(self):
        u = 0
        for i in range(self.V):
            if len(self.grafoAuxiliar[i]) % 2 != 0:
                u = i
                break
        print("\n")
        self.impressaoAux(u)