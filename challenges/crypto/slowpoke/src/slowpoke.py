flag = b"sstctf{x0r_is_1ts_0wn_1nv3rse}"

key = b'myKey'

ct = list(flag)
for i in range(76329456754327457328672853465324627534675147893128797562316437216752317656732167559801876498064713725178567321789672789674289077654871967236752761576823 % 2):
    newCt = []
    for j in range(len(ct)):
        newCt.append(ct[j]^key[j%len(key)])
    ct = newCt[:]
print(ct)