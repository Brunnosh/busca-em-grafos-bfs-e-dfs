import networkx as nx
import matplotlib.pyplot as plt

class VisualizarGrafo: 
    def __init__(self, grafo, inicio, fim):
        self.grafo = grafo
        self.inicio = inicio
        self.fim = fim

    # Função que cria o desenho gráfico utilizando a biblioteca NetworkX e Matplotlib
    def desenhar_grafo(self):
        grafo = self.grafo
        if grafo.qtdVertices > 500:
            print("Grafo muito grande para visualização!")
            return
        
        G = nx.Graph()
        for vertice, vizinhos in self.grafo.conexoes.items():
            for vizinho in vizinhos:
                G.add_edge(vertice, vizinho)
        pos = nx.spring_layout(G, seed=42, k=0.2)
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray",
                node_size=500, font_size=8)
        nx.draw_networkx_nodes(G, pos, nodelist=[self.inicio], node_color="red", node_size=700)
        nx.draw_networkx_nodes(G, pos, nodelist=[self.fim], node_color="green", node_size=700)
        plt.title("Grafo Gerado com Pontos de Início e Fim Destacados")
        plt.show()