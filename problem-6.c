#include <string.h>
#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(char *string){
    int l = strlen(string);
    bool isPal = true;
    for (int i = 0; i < l; i++) {
        isPal = isPal && (string[i] == string[l-i-1]);
    }
    return isPal;
}

int main(){
    int largestPal = 1;
    for (int i = 100; i < 1000; i++) {
        for (int j = 100; j < 1000; j++) {
            int k = i*j;
            if (k > largestPal) {
                char *strk;
                sprintf(strk, "%d", k);
                if (isPalindrome(strk)) {
                    largestPal = k;            
                }
            }
        }
    }
    printf("%d\n", largestPal);
    return 0;
}