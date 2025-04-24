#include <stdio.h>
#include <string.h>

void check_flag(char *input) {
    char key[7] = {0x5c, 0x52, 0x41, 0x37, 0x55, 0x3d, 0x30}; // XOR key ("\RA7U=0")
    char flag[22] = {0x2f, 0x21, 0x35, 0x54, 0x21, 0x5b, 0x4b, 0x24, 0x62, 0x33, 0x68, 0x64, 0x4e, 0x6f, 0x68, 0x3f, 0x75, 0x4d, 0x64, 0x53, 0x57, 0x21}; // Encrypted "sstctf{x0r_1s_4m4z1ng}"

    // Decrypt the flag using the XOR key
    for (int i = 0; i < sizeof(flag); i++) {
        flag[i] ^= key[i % sizeof(key)];
    }

    // Ensure the string is null-terminated by explicitly setting the last byte to '\0'
    flag[sizeof(flag) - 1] = '\0'; // Set last byte to null terminator

    // Compare the user input with the decrypted flag
    if (strncmp(input, flag, strlen(flag)) == 0) {  // Use strlen to handle correct length
        printf("Correct! Flag is: %s\n", input);
    } else {
        printf("Incorrect! Try again.\n");
    }
}

int main() {
    char user_input[50];

    printf("Enter the flag: ");
    scanf("%49s", user_input);

    check_flag(user_input);

    return 0;
}
