#include <string.h>
#include <stdio.h>


int main(){
    int a = 1;
    int b = 1;
    int sum = 0;
    while (b < 4000000) {
        int t = a + b;
        a = b;
        b = t;
        if (t % 2 == 0) {
            sum += t;
        }
    }
    printf("%d\n", sum);
    return 0;
}