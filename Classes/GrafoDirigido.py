from Classes.Aresta import Aresta
from Classes.Vertice import Vertice

class  GrafoDirigido:
    def __init__(self,nomeArquivo):
        try:
            arquivo = open(f"../Arquivos_grafos_dirigidos/{nomeArquivo}"+".txt", "r").readlines()
        except Exception:
            try:
                arquivo = open(f"Arquivos_grafos_dirigidos/{nomeArquivo}" + ".txt", "r").readlines()
            except Exception:
                print("\n::::::::: Arquivo não existente ::::::::::\n")
                exit(1)

        self.ordem = int(arquivo[0].replace('\n', ''))
        self.tamanho = len(arquivo)
        self.vertices = []
        self.arestas = []
        self.grafo = [[0 for i in range(self.ordem)] for j in range(self.ordem)]
        for i in range(1, self.tamanho):
            linha = arquivo[i].split()
            self.grafo[(int(linha[0])) - 1][(int(linha[1]) - 1)] = int(linha[2])

        for i in range(self.ordem):
            self.vertices.append(Vertice(i + 1))

        for i in range(1, len(arquivo)):
            linha = arquivo[i].split()
            self.arestas.append(Aresta(linha[0], linha[1], linha[2], i))
            self.vertices[int(linha[0]) - 1].somaGrau()
            self.vertices[int(linha[0]) - 1].adicionaVizinho(linha[1])


    def haveCicle(self):
        fila = []
        visitado = []
        fila.append(1)
        while len(fila) != 0:
            value = fila[0]
            fila.pop(0)
            visitado.append(value)
            aD = self.vertices[value - 1].getVizinhos()
            for item in aD:
                item = int(item)
                if item in visitado:
                    return True
                fila.append(item)

        return False

    def ordenacao_topologica(self):
        # pegar o vertice com menor grau e tira o vertice do grafo
        grafo1 = self.grafo
        R = []
        N = [i for i in range(1, self.ordem + 1)]
        for i in range(self.ordem):
            menor = self.pegarVerticeMenorGrau(grafo1, N)
            R.append(menor)
            removeDaLista(N,menor)
            self.tirarMenorDag(grafo1, menor)

        print(R)

    def tirarMenorDag(self, grafo, menor):
        for i in range(self.ordem):
            grafo[menor - 1][i] = 0

    def pegarVerticeMenorGrau(self, grafo, N):
        cont = 0
        maiorCont = 999
        menor = None
        for vertice in N:
            for vertice2 in N:
                if grafo[int(vertice2)- 1][int(vertice)- 1] != 0:
                    cont += 1

            if cont < maiorCont:
                menor = vertice
                maiorCont = cont
            cont = 0
        return menor

    def printGrafo(self):
        for line in self.grafo:
            print('  '.join(map(str, line)))

def removeDaLista(Lista,valor):
    pos = 0
    for v in Lista:
        if int(v) == int(valor):
            del(Lista[pos])

        pos += 1










