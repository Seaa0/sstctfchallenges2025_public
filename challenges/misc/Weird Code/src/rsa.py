from Crypto.Util.number import getPrime
flag = 'sstctf{pl3as3_don+_wr1te_c0de_lik3_th15...}'
p = getPrime(10)
q = getPrime(10)
N = p*q
e = 65537
phi = (p-1)*(q-1)
print(pow(e,-1,phi))
print(N)
output = ''
for ch in flag:
    output += chr(pow(ord(ch),e,N))

print(output.encode())
