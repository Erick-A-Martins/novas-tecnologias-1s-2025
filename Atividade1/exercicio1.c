#include <stdio.h>

int main () {
    long num, aux, count = 0, div = 10;

    printf("Digite um numero: ");
    scanf("%ld", &num);

    aux = num;

    while(aux != 0) {
        count++;
        aux = num/div;
        div = div * 10;
    }

    div = div/10;

    for(int i = 1; i <= count; i++) {
        div /= 10;
        printf("%ld\n", num/div);
        num %= div;
    }

    return 0;
}