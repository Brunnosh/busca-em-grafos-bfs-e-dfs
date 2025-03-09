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
        grau = {v: 0 for v in range(self.qtdVertices)}

        # Passo 2: Garantir que o grafo seja conexo criando uma cadeia inicial de conexões
        for i in range(self.qtdVertices - 1):
            self.adicionar_aresta(i, i + 1)
            grau[i] += 1
            grau[i + 1] += 1

        # Passo 3: Criar a lista de nós que ainda precisam de mais conexões
        nos_disponiveis = [v for v in range(self.qtdVertices) if grau[v] < num_arestas]

        # Passo 4: Continuar adicionando arestas até que cada nó tenha o número correto de conexões
        while len(nos_disponiveis) > 1:
            origem, destino = random.sample(nos_disponiveis, 2)

            if destino not in self.conexoes[origem]:  # Evita duplicatas
                self.adicionar_aresta(origem, destino)
                grau[origem] += 1
                grau[destino] += 1

                # Se algum nó atingir o limite de conexões, removemos da lista de disponíveis
                if grau[origem] >= num_arestas:
                    nos_disponiveis.remove(origem)
                if grau[destino] >= num_arestas:
                    nos_disponiveis.remove(destino)

    # Imprime todas as conexões (arestas) que foram criadas
    def imprimir_conexoes(self):
        print("\nGrafo gerado (representação no terminal):")
        for vertice, vizinhos in sorted(self.conexoes.items()):
            print(f"{vertice}: {sorted(vizinhos)}")