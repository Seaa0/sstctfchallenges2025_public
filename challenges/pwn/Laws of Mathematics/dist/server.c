#include <stdio.h>

int main() {
    char* flag = "sstctf{REDACTED}";
    printf("Enter your favourite number: ");
    int myNumber;
    scanf("%d",&myNumber);
    int myNumberAdded = myNumber+1;
    if (myNumberAdded < myNumber) {
        printf("How did you break the laws of mathematics??\n");
        printf("%s\n",flag);
    } else {
        printf("%d\n",myNumberAdded);
    }
    return 0;
}