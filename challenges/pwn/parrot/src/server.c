#include <stdio.h>

int main() {
    char* flag = "sstctf{1nt3ger_overfl0w_br34ks_th3_law5_0f_m4+h}";
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