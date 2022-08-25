#include <string.h>
#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n) {
    if (n == 2) {
        return true;
    }
    if (n == 0 || n == 1 || n % 2 == 0) {
        return false;
    } else {
        for (int i = 3; i < n; i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

int main(){
    int count = 0;
    int i = 1;
    while (count != 10001) {
        if (isPrime(i)) {
            count++;
        }
        i++;
    }
    printf("%d\n", i-1);
    return 0;
}