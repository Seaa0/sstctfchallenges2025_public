# Slowpoke

XOR Operations are in play here.
(Explain more about XOR here)

Solve script
```py
ct = [30, 10, 63, 6, 13, 11, 2, 51, 85, 11, 50, 16, 56, 58, 72, 25, 10, 20, 85, 14, 3, 38, 122, 11, 15, 94, 11, 56, 0, 4]

key = b'myKey'

flag = b''

# only need to xor once because (a^b)^b = a

for i in range(len(ct)):
    flag += int.to_bytes(ct[i]^key[i%len(key)])

print(flag
```