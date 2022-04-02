class Vertice:
    def __init__(self,id):
        self.id = id
        self.grau = 0
        self.vizinhos = []
    
    def somaGrau(self):
        self.grau+=1

    def getGrau(self):
        return self.grau

    def adicionaVizinho(self,vizinho):
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)
        else:
            return
    
    def getVizinhos(self):
        return self.vizinhos