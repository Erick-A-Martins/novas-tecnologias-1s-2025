#include <stdio.h>

int pred (int n) {
    return --n;
}

int suc (int n) {
    return ++n;
}

int soma (int n1, int n2) {

    if(n1 == 0) 
        return n2;
    else
        return soma(pred(n1), suc(n2));

    // while(n1 != 0) {
    //     n1 = pred(n1);
    //     n2 = suc(n2);
    // }

    // return n2;
} 

int main() {

    int n1, n2;
    printf("Digite o numero: ");
    scanf("%d+%d", &n1, &n2);

    printf("%d+%d = %d", n1, n2, soma(n1, n2));

    return 0;
}