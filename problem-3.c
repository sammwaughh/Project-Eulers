#include <string.h>
#include <stdio.h>
#include <stdbool.h>

int main(){
    int factors[100];
    int index = 0;
    int maxFactor = 1;
    long num = 600851475143;

    while (num != 1) {
        int f = 2;
        bool found = false;
        while (!found) {
            if (num % f == 0) {
                num = num / f;
                factors[index] = f;
                index += 1;
                found = true;
                if (f > maxFactor) {
                    maxFactor = f;
                }
            } else {
                f += 1;
            }
        }
    }
    printf("%d\n", maxFactor);
    return 0;
}