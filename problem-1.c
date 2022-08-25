#include <string.h>
#include <stdio.h>

int findSum(){
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}


int main(){
    int sum = findSum();
    printf("%d\n", sum);
    return 0;
}