#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef struct Node {
    int numNo;
    struct Node* proximoNo;
} Node;

typedef struct Grafo {
    int qtdNode;
    Node** listaAdj;

} Grafo;

void escolhaInicial(int *numVertices,int *edgesPerNode){

    bool flag = true;



    printf("Número de vértices (500, 5000, 10000): ");
    scanf("%d", numVertices);
    printf("Número de arestas por nó (3, 5, 7): ");
    scanf("%d", edgesPerNode);

    if ((*numVertices != 500 && *numVertices != 5000 && *numVertices != 10000) ||
    (*edgesPerNode != 3 && *edgesPerNode != 5 && *edgesPerNode != 7)) {
    flag = false;
    }

    while (flag == false){
        printf("Entrada inválida! Use valores permitidos.\n");
        printf("Número de vértices (500, 5000, 10000): ");
        scanf("%d", *numVertices);
        printf("Número de arestas por nó (3, 5, 7): ");
        scanf("%d", *edgesPerNode);
        if ((*numVertices != 500 && *numVertices != 5000 && *numVertices != 10000) ||
        (*edgesPerNode != 3 && *edgesPerNode != 5 && *edgesPerNode != 7)) {
        flag = false;
        }else{
            flag = true;
        }
        
    }

}

int main(){
    int numVertices, edgesPerNode;
    escolhaInicial(&numVertices, &edgesPerNode);

    printf("%d", numVertices);
    printf("%d", edgesPerNode);



    return 0;
}

