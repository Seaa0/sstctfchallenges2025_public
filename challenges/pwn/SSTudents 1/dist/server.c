#include <stdio.h>
#include <string.h>

int main() {
    char flag[168] = "sstctf{REDACTED}";
    char username[6];
    char password[168];
    int authenticated;
    gets(username);
    gets(password);
    authenticated = !(strcmp(username,"admin") || (strcmp(password,flag))) || authenticated; // thanks demorgen's theorem!
    if (authenticated) {
        printf("I don't know why you would need the password if you can log in, but here it is!\n");
        printf("%s\n",flag);
    }
}