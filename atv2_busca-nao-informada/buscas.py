import time
from collections import deque

class Buscas:
    def __init__(self, grafo):
        self.grafo = grafo

    # Busca em Largura
    def busca_em_largura(self, inicio, objetivo):
        visitados = {v: False for v in self.grafo.conexoes}
        distancia = {v: float('inf') for v in self.grafo.conexoes}
        anterior = {v: None for v in self.grafo.conexoes}

        caminho = [] 

        fila = deque([inicio])
        visitados[inicio] = True
        distancia[inicio] = 0

        inicio_tempo = time.perf_counter()
        while fila:
            atual = fila.popleft()
            caminho.append(atual)

            if atual == objetivo:
                break

            for vizinho in self.grafo.conexoes[atual]:
                if not visitados[vizinho]:
                    visitados[vizinho] = True
                    distancia[vizinho] = distancia[atual] + 1
                    anterior[vizinho] = atual
                    fila.append(vizinho)

        tempo_execucao = time.perf_counter() - inicio_tempo

        return caminho, distancia[objetivo], tempo_execucao
    
    # Busca em Profundidade
    def busca_em_profundidade(self, inicio, objetivo):
        visitados = {v: False for v in self.grafo.conexoes}
        caminho = []

        def _dfs(v):
            if visitados[v]:
                return False
            visitados[v] = True
            caminho.append(v)
            if v == objetivo:
                return True
            for vizinho in self.grafo.conexoes[v]:
                if _dfs(vizinho):
                    return True
            caminho.pop()
            return False

        _dfs(inicio)
        return caminho

    # Busca em Profundidade Limitada
    def busca_em_profundidade_limitada(self, inicio, objetivo, limite):
        visitados = {v: False for v in self.grafo.conexoes}
        caminho = []

        def _dfs(v, profundidade):
            if profundidade > limite:
                return False
            if visitados[v]:
                return False
            visitados[v] = True
            caminho.append(v)
            if v == objetivo:
                return True
            for vizinho in self.grafo.conexoes[v]:
                if _dfs(vizinho, profundidade + 1):
                    return True
            caminho.pop()
            return False

        _dfs(inicio, 0)
        return caminho