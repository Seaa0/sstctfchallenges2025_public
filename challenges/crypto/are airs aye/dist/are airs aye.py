from Crypto.Util.number import bytes_to_long, getPrime

flag = b'sstctf{REDACTED}'
flag = flag[7:-1]

p = getPrime(64)
q = getPrime(64)
N = p*q
e = 65537

m = bytes_to_long(flag)
assert m < N
ct = pow(m,e,N)

print('N =',N)
print('ct =',ct)
# N = 193686257153450498709596628360387541709
# ct = 44648706095035340653015983461991571365