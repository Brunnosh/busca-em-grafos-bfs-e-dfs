import networkx as nx
import random
import sys
import matplotlib.pyplot as plt

def gerar_grafo(num_vertices, arestas_por_vertice):
    G = nx.Graph()
    
    # Adiciona os vértices e o atributo 'objetivo' para cada nó
    for i in range(num_vertices):
        G.add_node(i, objetivo=False)
    
    # Escolhe aleatoriamente um nó para ser o objetivo
    nodo_objetivo = random.randint(0, num_vertices - 1)
    G.nodes[nodo_objetivo]['objetivo'] = True  # Marca o nó como objetivo
    
    print(f"\nO nó {nodo_objetivo} foi marcado como o nó objetivo!")

    # Adiciona as arestas com feedback de progresso
    for v in range(num_vertices):
        conexoes = set()
        while len(conexoes) < arestas_por_vertice:
            u = random.randint(0, num_vertices - 1)
            if u != v and u not in conexoes:
                G.add_edge(v, u)
                conexoes.add(u)
        
    print("\nGrafo gerado com sucesso!")  
    return G




def buscaEmBFS():
    return 0




def buscaEmDFS():
    return 0



if __name__ == "__main__":
    vertices = [500,5000,10000]
    arestas = [3,5,7]

    print("Escolha uma das 3 opções: ", vertices)
    escolhaVertice = int(input())
    while escolhaVertice not in [1,2,3]:
        print("Escolha entre 1,2 e 3")
        escolhaVertice = int(input())

    print("Escolha uma das 3 opções: ", arestas)
    escolhaAresta = int(input())
    while escolhaAresta not in [1,2,3]:
        print("Escolha entre 1,2 e 3")
        escolhaAresta = int(input())

    grafo = gerar_grafo(vertices[escolhaVertice-1],arestas[escolhaAresta-1])
    
    print("Arestas do grafo:", list(grafo.edges))

    for node in grafo.nodes(data=True):
        if node[1]['objetivo']:
            print(f"Nó objetivo: {node[0]}")
        
    