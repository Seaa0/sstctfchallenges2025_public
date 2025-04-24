// doesn't compile properly on apple silicon macs (code still runs but exploit doesn't work)
// run the dockerfile if on apple silicon mac
// compile cmd: gcc server.c -std=c99 -o server
#include <stdio.h>
#include <string.h>

int main() {
    char flag[168] = "sstctf{1_h0p3_y0u_d1dn't_+ry_t0_brut3_f0rc3_th1s_fl4g_becaus3_i_m4de_it_unnec3s5s4rily_l0ng_43821578927892678325786256738672357698526978768532532486721067842317853217}";
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