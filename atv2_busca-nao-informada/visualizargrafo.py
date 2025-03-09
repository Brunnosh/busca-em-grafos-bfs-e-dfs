# import networkx as nx
# import matplotlib.pyplot as plt

# class VisualizarGrafo: 
#     def __init__(self, grafo, inicio, fim):
#         self.grafo = grafo
#         self.inicio = inicio
#         self.fim = fim

#     # Função que cria o desenho gráfico utilizando a biblioteca NetworkX e Matplotlib
#     def desenhar_grafo(self):
#         if self.grafo.qtdVertices > 500:
#             print("Grafo muito grande para visualização!")
#             return
        
#         G = nx.Graph()

#         for vertice, vizinhos in self.grafo.conexoes.items():
#             for vizinho in vizinhos:
#                 G.add_edge(vertice, vizinho)

#         pos = nx.spring_layout(G, seed=42, k=0.2)
#         plt.figure(figsize=(12, 8))
#         nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray",
#                 node_size=500, font_size=8)

#         if self.inicio is not None:
#             nx.draw_networkx_nodes(G, pos, nodelist=[self.inicio], node_color="red", node_size=700)
#         if self.fim is not None:
#             nx.draw_networkx_nodes(G, pos, nodelist=[self.fim], node_color="green", node_size=700)

#         plt.title("Grafo Gerado com Pontos de Início e Fim Destacados")
#         plt.show(). 

import os
import webbrowser
from pyvis.network import Network

class VisualizarGrafo:
    def __init__(self, grafo, inicio=None, fim=None):
        self.grafo = grafo
        self.inicio = inicio
        self.fim = fim

    def desenhar_grafo(self, nome_arquivo="grafo/grafo.html"):
        if not os.path.exists("grafo"):
            os.makedirs("grafo")

        net = Network(height="800px", width="100%", notebook=False, directed=False)
        
        # Adiciona os nós ao grafo
        for vertice in self.grafo.conexoes.keys():
            cor = "lightblue"
            if vertice == self.inicio:
                cor = "red"  # Nó inicial
            elif vertice == self.fim:
                cor = "green"  # Nó final

            # Adiciona o nó com o número dentro (label configurado para aparecer no centro)
            net.add_node(vertice, label=str(vertice), color=cor, font={'size': 20, 'color': 'black', 'background': 'white', 'strokeWidth': 2, 'strokeColor': 'black'})

        # Adiciona as conexões
        for vertice, vizinhos in self.grafo.conexoes.items():
            for vizinho in vizinhos:
                net.add_edge(vertice, vizinho)

        # Adiciona uma legenda para indicar onde começa e termina
        # Adicionando nós extras apenas para legenda
        net.add_node('Inicio', label="Início", color="red", shape="box")
        net.add_node('Fim', label="Fim", color="green", shape="box")
        net.add_edge('Inicio', 'Fim', arrows='to', color="black", dashes=True)

        # Desativa a física para tornar o grafo fixo
        net.toggle_physics(False)

        try:
            net.write_html(nome_arquivo)  # Salva o HTML
            print(f"Grafo salvo como {nome_arquivo}. Abra no navegador para visualizar.")
            webbrowser.open(os.path.abspath(nome_arquivo))

        except Exception as e:
            print(f"Erro ao salvar o grafo: {e}")

