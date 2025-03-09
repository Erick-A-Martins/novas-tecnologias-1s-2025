#include <stdio.h>

void torreHannoi (int discos, char origem, char auxiliar, char destino) {
    if(discos == 1)
    {
        printf("O disco 1 foi de A para C: \n");
        return;
    }   

    printf("O disco %d foi de %c para %c.\n", discos, origem, auxiliar);

    torreHannoi(discos-1, auxiliar, destino, origem);

    printf("O disoc %d foi de %c para %c\n", discos, auxiliar, destino);
}

int main () {
    int discos;
    printf("insira o numero de discos: ");
    scanf("%d", &discos);

    torreHannoi(discos, 'A', 'B', 'C');
    


    return 0;
}