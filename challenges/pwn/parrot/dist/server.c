#include <stdio.h>

int main() {
    char* flag = "sstctf{REDACTED}";
    while (1) {
        char input[32];
        printf("I repeat what you say: ");
        fgets(input, sizeof(input) - 1, stdin);
        printf(input);
        printf("\n");
    }
    return 0;
}