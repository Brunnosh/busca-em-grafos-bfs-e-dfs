import random
import time
from grafo import Grafo
from visualizargrafo import VisualizarGrafo
from buscas import Buscas

def obter_dados_usuario():
    while True:
        num_vertices = int(input("Número de vértices (15, 500, 5000, 10000): "))
        while num_vertices not in {15, 500, 5000, 10000}:
            print("Entrada inválida! Escolha entre 15, 500, 5000, 10000.")
            num_vertices = int(input("Número de vértices: "))

        num_arestas = int(input("Número de arestas por nó (3, 5, 7): "))
        while num_arestas not in {3, 5, 7}:
            print("Entrada inválida! Escolha entre 3, 5, 7.")
            num_arestas = int(input("Número de arestas por nó: "))

        return num_vertices, num_arestas

def sortear_pontos(grafo):
    pontos = list(grafo.conexoes.keys())
    inicio = random.choice(pontos)
    fim = random.choice(pontos)
    
    while inicio == fim:
        fim = random.choice(pontos)

    return inicio, fim


def executar():
    while True:
        num_vertices, num_arestas = obter_dados_usuario()

        grafo = Grafo(num_vertices)
        grafo.gerar_arestas_aleatorias(num_arestas)

        print("\nGrafo gerado!")
        grafo.imprimir_conexoes()

        inicio, fim = sortear_pontos(grafo)
        print(f"\nPonto de início: {inicio}")
        print(f"Ponto final: {fim}")

        buscas = Buscas(grafo)

        # Busca em Largura
        print("\nExecutando a Busca em Largura...")
        bfs_time_start = time.time()
        caminho_bfs, dist_bfs = buscas.busca_em_largura(inicio, fim)
        bfs_time_end = time.time()
        print(f"Caminho da Busca em Largura: {caminho_bfs}")
        print(f"Distância: {dist_bfs}")
        print(f"Tempo de execução da Busca em Largura: {bfs_time_end - bfs_time_start:.6f} segundos")
        print(f"Tamanho do caminho (BFS): {len(caminho_bfs)}")

        # Busca em Profundidade
        print("\nExecutando a Busca em Profundidade...")
        dfs_time_start = time.time()
        caminho_dfs = buscas.busca_em_profundidade(inicio, fim)
        dfs_time_end = time.time()
        print(f"Caminho da Busca em Profundidade: {caminho_dfs}")
        print(f"Tempo de execução da Busca em Profundidade: {dfs_time_end - dfs_time_start:.6f} segundos")
        print(f"Tamanho do caminho (DFS): {len(caminho_dfs)}")

        # Busca em Profundidade Limitada
        # limite = 3
        # print(f"\nExecutando a Busca em Profundidade Limitada com limite {limite}...")
        # start_time = time.time()
        # caminho_dfs_limitada = buscas.busca_em_profundidade_limitada(inicio, fim, limite)
        # dfs_limitada_time = time.time() - start_time
        # print(f"Caminho da Busca em Profundidade Limitada: {caminho_dfs_limitada}")
        # print(f"Tempo de execução da Busca em Profundidade Limitada: {dfs_limitada_time:.6f} segundos")
        # print(f"Tamanho do caminho (DFS Limitada): {len(caminho_dfs_limitada)}")

        visualizador = VisualizarGrafo(grafo, inicio, fim)
        print("\nDesenhando o grafo...")
        visualizador.desenhar_grafo()

        repetir = input("\nDeseja gerar outro grafo? (s/n): ").strip().lower()
        if repetir == 'n':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    executar()