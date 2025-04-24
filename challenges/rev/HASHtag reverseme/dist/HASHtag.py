from hashlib import sha256

flag = b'sstctf{XXXXX}'
flag = flag[7:-1]

assert len(flag) == 5
assert flag.isalnum() 
assert flag == flag.lower()

print(sha256(flag).hexdigest())
# 6e06211fc4a1fcc363c7eb6e69f48353bbb05bb16b6b44795e023c6536d51f33