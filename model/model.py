import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.squadre=DAO.getSquadre()
        self.grafo = nx.Graph()
        self._idMap = {}


    def creaGrafo(self, squadra):
        self.nodi = DAO.getNodi(squadra)[0]
        self.peso =DAO.getNodi(squadra)[1]
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                        self.grafo.add_edge(nodo1, nodo2, weight=abs(self.peso[nodo1]-self.peso[nodo2]))

    def analisi(self,anno):
        dizio={}
        for nodo in self.grafo.neighbors(anno):
            dizio[nodo]=self.grafo[nodo][anno]["weight"]
        dizioOrder=sorted(dizio.items(),key=lambda item:item[1],reverse=True)
        return dizioOrder