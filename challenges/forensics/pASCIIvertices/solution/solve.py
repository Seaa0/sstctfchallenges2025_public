with open('peskyVertices.obj', 'r') as f:
    data = f.read()

data = data.split('\n\n')
data = data[-1]

data = data.split('\n')[1:]

flag = ''

for vertex in data:
    ch = vertex[2:6]
    if ch:
        ch = float(ch)
        ch = round(ch*100)
        flag += chr(ch)
print(flag)