#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef struct No {
    int numNo;  // Identificador do nó
    int qtdConexoes;  // Número de conexões (arestas)
    struct No** conexoes;  // Ponteiro para array de ponteiros para os nós conectados
} No;

typedef struct Grafo {
    int qtdNode;
    No** listaAdj;

} Grafo;

void userInput(int* numVertices, int* edgesPerNode) {
    bool flag = true;

    while (flag) {
        printf("Número de vértices (5, 500, 5000, 10000): ");
        scanf("%d", numVertices);
        printf("Número de arestas por nó (3, 5, 7): ");
        scanf("%d", edgesPerNode);

        if ((*numVertices != 5 && *numVertices != 500 && *numVertices != 5000 && *numVertices != 10000) ||
            (*edgesPerNode != 3 && *edgesPerNode != 5 && *edgesPerNode != 7)) {
            printf("Entrada inválida! Use valores permitidos.\n");
        } else {
            flag = false;  
        }
    }
}

struct No * criarNo(int numeroNo, int maxArestas){
    No* no = (No*)malloc(sizeof(No));
    no ->numNo = numeroNo;
    no->qtdConexoes = 0; //inicia com zero conexões
    no->conexoes = (No**)malloc(maxArestas * sizeof(No*));; //Array com ponteiros de outros nós iniciado vazio
    return no;

}

struct Grafo * criarGrafo(int V, int maxArestas){
    //Aloca memória da struct grafo
    struct Grafo* G = (struct Grafo*)malloc(sizeof(struct Grafo));
    G->qtdNode = V;

    //Aloca a memoria da lista de adjacencia
    G->listaAdj = (struct No**)malloc(V*sizeof(struct No*));

    for (int i = 0; i < V; i++) {
        G->listaAdj[i] = criarNo(i, maxArestas);
    }
    return G;

}

void imprimirGrafo(Grafo* G) {
    for (int i = 0; i < G->qtdNode; i++) {
        No* no = G->listaAdj[i];
        printf("Nó %d -> ", no->numNo);
        for (int j = 0; j < no->qtdConexoes; j++) {
            printf("%d ", no->conexoes[j]->numNo);
        }
        printf("\n");
    }
}

void adicionarAresta(No* origem, No* destino) {
    origem->conexoes = (No**)realloc(origem->conexoes, (origem->qtdConexoes + 1) * sizeof(No*));
    origem->conexoes[origem->qtdConexoes] = destino;
    origem->qtdConexoes++;  // Incrementa o número de conexões
}

bool arestaExiste(No* origem, No* destino) {
    for (int i = 0; i < origem->qtdConexoes; i++) {
        if (origem->conexoes[i] == destino) {
            return true;  
        }
    }
    return false;  
}

void popularGrafo(Grafo* G, int arestasPorNo) {
    for (int i = 0; i < G->qtdNode; i++) {
        // Aloca memória para as conexões do nó atual
        G->listaAdj[i]->qtdConexoes = arestasPorNo;
        
        
        int conexoesFeitas = 0;
        while (conexoesFeitas < arestasPorNo) {
            // Gera um destino aleatório
            int destinoIndex = rand() % G->qtdNode;
            
            // Evita conectar o nó a si mesmo
            if (destinoIndex != i) {
                // Verifica se a conexão já existe
                bool conexaoExistente = arestaExiste(G->listaAdj[i], G->listaAdj[destinoIndex]);
                // Se a conexão não existir, cria a conexão
                if (!conexaoExistente) {
                    G->listaAdj[i]->conexoes[conexoesFeitas] = G->listaAdj[destinoIndex];
                    conexoesFeitas++;
                }
            }
        }
    }
}



int main(){
    int numVertices, edgesPerNode;
    Grafo *G;
    userInput(&numVertices, &edgesPerNode);

    G = criarGrafo(numVertices, edgesPerNode);

    //adicionarAresta(G->listaAdj[0],G->listaAdj[1]);
    srand(time(NULL));
    popularGrafo(G, edgesPerNode);

    imprimirGrafo(G);

    printf("%d", numVertices);
    printf("%d", edgesPerNode);





    return 0;
}

