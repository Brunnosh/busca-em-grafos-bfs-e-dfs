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
                cor = "purple"  # Nó inicial
            elif vertice == self.fim:
                cor = "green"  # Nó final

            net.add_node(
                vertice, 
                label=str(vertice), 
                color=cor, 
                font={'size': 20, 'color': 'black', 'strokeWidth': 2, 'strokeColor': 'black'},
                shape="circle",
                size=30
            )

        # Adiciona as conexões
        for vertice, vizinhos in self.grafo.conexoes.items():
            for vizinho in vizinhos:
                net.add_edge(vertice, vizinho)

        # Desativa a física para melhorar a performance
        net.toggle_physics(True)

        try:
            net.write_html(nome_arquivo)
            print(f"Grafo salvo como {nome_arquivo}.")
            self.adicionar_legenda(nome_arquivo)
            webbrowser.open(os.path.abspath(nome_arquivo))

        except Exception as e:
            print(f"Erro ao salvar o grafo: {e}")

    def adicionar_legenda(self, nome_arquivo):
        """Função para adicionar a legenda diretamente no HTML gerado"""
        with open(nome_arquivo, 'r') as file:
            html_content = file.read()

        legenda_html = """
        <div style="position: absolute; top: 20px; left: 20px; background-color: white; border: 1px solid #ccc; padding: 10px; z-index: 10;">
            <h3>Legenda</h3>
            <p><strong style="background-color: purple; color: white; padding: 5px;">Inicio</strong></p>
            <p><strong style="background-color: green; color: white; padding: 5px;">Fim</strong></p>
        </div>
        """

        # Adiciona a legenda antes da tag </body> no HTML
        html_content = html_content.replace('</body>', legenda_html + '</body>')

        # Reescreve o arquivo HTML com a legenda
        with open(nome_arquivo, 'w') as file:
            file.write(html_content)
