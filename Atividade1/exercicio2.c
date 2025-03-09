#include <stdio.h>

int main () {
    int num, quad = 0;

    printf("Digite o numero: ");
    scanf("%d", &num);

    for(int i = 1, j= 1; j <= num; i+=2, j++) {
        quad = quad + 1;
    }

    printf("%d^2 = %d",  num, quad);

    return 0;
}