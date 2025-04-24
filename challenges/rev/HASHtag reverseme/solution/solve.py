from hashlib import sha256

possibleChars = 'abcdefghijklmnopqrstuvwxyz1234567890'

for i in possibleChars:
    for j in possibleChars:
        for k in possibleChars:
            for l in possibleChars:
                for m in possibleChars:
                    flag = (i+j+k+l+m).encode()
                    if sha256(flag).hexdigest() == '6e06211fc4a1fcc363c7eb6e69f48353bbb05bb16b6b44795e023c6536d51f33':
                        print('sstctf{'+flag.decode()+'}')
                        exit()