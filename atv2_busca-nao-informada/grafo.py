import random

class Grafo:
    # Função que inicializa número fixo de vértices e cria lista de arestas vazias
    def __init__(self, num_vertices):
        self.qtdVertices = num_vertices
        self.conexoes = {i: set() for i in range(num_vertices)}

    # Função que adiciona aresta entre dois vértices
    def adicionar_aresta(self, origem, destino):
        if origem != destino and destino not in self.conexoes[origem]:
            self.conexoes[origem].add(destino)
            self.conexoes[destino].add(origem)

    # Função que gera o grafo garantindo que cada nó tenha exatamente o número correto de arestas
    def gerar_arestas_aleatorias(self, num_arestas):
        todos_os_nos = list(self.conexoes.keys())
        
        for i in range(self.qtdVertices - 1):
            self.adicionar_aresta(i, i + 1)

        nos_disponiveis = [n for n in todos_os_nos if len(self.conexoes[n]) < num_arestas]

        while len(nos_disponiveis) > 1:
            origem, destino = random.sample(nos_disponiveis, 2)

            self.adicionar_aresta(origem, destino)

            if len(self.conexoes[origem]) >= num_arestas:
                nos_disponiveis.remove(origem)
            if len(self.conexoes[destino]) >= num_arestas:
                nos_disponiveis.remove(destino)

    # Imprime todas as conexões (arestas) que foram criadas
    def imprimir_conexoes(self):
        for vertice, vizinhos in sorted(self.conexoes.items()):
            print(f"{vertice}: {sorted(vizinhos)}")