# Are Airs Aye

This challenge is a simple RSA Challenge
(Talk more about RSA and give an explanation of the attack here)

Solve Script:
```py
from Crypto.Util.number import long_to_bytes
N = 193686257153450498709596628360387541709
ct = 44648706095035340653015983461991571365
e = 65537

# N was factorised using https://www.alpertron.com.ar/ECM.HTM
p = 12535406567654215837
q = 15451134840191747057

phi = (p-1)*(q-1)
d = pow(e,-1,phi)
m = pow(ct,d,N)
print('sstctf{'+long_to_bytes(m).decode()+'}')
```