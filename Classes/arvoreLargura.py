class Node:
    def __init__(self, vertice):
        self.vertice = vertice
        self.conecao = {vertice:[]}


class __TreeWidth:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node

        elif data:
            self.root = Node(data)

        else:
            self.root = None

    def imprimir(self,vertice=None,lista=None):
        if vertice is None:
            aux = self.root
            lista = list()

        else:
            aux = vertice
            print('\n')

        lista.append(aux.vertice)

        print(f"Vertice {aux.vertice}")

        for kid in aux.conecao[aux.vertice]:
            print(kid.vertice,end=' ')

        for kid in aux.conecao[aux.vertice]:
            if kid.vertice not in lista:
                self.imprimir(kid,lista)


class TreeWidth(__TreeWidth):

    def __init__(self):
        super().__init__()
        self.explorados = list()

    def start(self,vertice):
        self.root = Node(vertice)

    def explorar(self,vertice,verticeFilho,pos=None):
        filho = Node(verticeFilho)
        if pos is None:
            aux = self.root
        else:
            aux = pos


        if vertice in aux.conecao:
            for kid in aux.conecao[aux.vertice]:
                if kid.vertice == vertice:
                    return False
            aux.conecao[vertice].append(filho)
            self.addExplore(vertice,verticeFilho)
            return True

        else:
            for kid in aux.conecao[aux.vertice]:
                self.explorar(vertice,verticeFilho,kid)


    def addExplore(self,pai,filho):
        self.explorados.append([pai,filho])

    def areExplore(self,pai,filho):
        return [pai,filho] in self.explorados or [filho,pai] in self.explorados