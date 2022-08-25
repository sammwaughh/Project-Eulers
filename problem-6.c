#include <string.h>
#include <stdio.h>
#include <stdbool.h>

int main(){
    int squareSum = 0;
    int sum = 0;
    for (int i = 1; i < 101; i++) {
        sum += i;
        squareSum += i*i;
    }
    int ans = sum*sum - squareSum;
    printf("%d\n", ans);
    return 0;
}