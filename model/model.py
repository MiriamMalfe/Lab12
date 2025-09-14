import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def listaNazione(self):
        return DAO.getNazione()

    def listaAnni(self):
        return DAO.getAnno()

    def aggiungiNodi(self, nazione):
        listaNodi = DAO.getRetailerPerNazione(nazione)
        self.grafo.add_nodes_from(listaNodi)

    def aggiungiArchi(self, anno):
        listaNodi = list(self.grafo.nodes)

        for n1 in listaNodi:
            for n2 in listaNodi:
                if n1.Retailer_code == n2.Retailer_code:
                    pass
                else:
                    peso = 0
                    prodotti1 = DAO.getListaProdotti(n1.Retailer_code, anno)
                    prodotti2 = DAO.getListaProdotti(n2.Retailer_code, anno)
                    for p1 in prodotti1:
                        for p2 in prodotti2:
                            if p1 == p2:
                                peso +=1
                    if peso > 0:
                        self.grafo.add_edge(n1, n2, weight=peso)

    def creaGrafo(self, nazione, anno):
        self.aggiungiNodi(nazione)
        self.aggiungiArchi(anno)
        print(f"il numero di nodi è: {self.grafo.number_of_nodes()}")
        print(f"il numero di archi è: {self.grafo.number_of_edges()}")

    def volume(self):
        listaNodi = list(self.grafo.nodes)

        stringa = "Volumi di vendita: "
        diz = {}
        for n in listaNodi:

            diz[n] = self.grafo.degree(n, weight='weight')

        for k,v in sorted(diz.items(), key=lambda item: item[1], reverse=True):
            stringa = stringa+ f"\n{k.Retailer_name} {v}"
        return stringa
