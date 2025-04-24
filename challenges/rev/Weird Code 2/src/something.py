import base64

flag = "sstctf{0b4fusc@t1on_t0g3ther_w1th_jsf_1s_@_b@d_1d3@}"
flag = base64.b64encode(flag.encode()).decode()
flag = flag[::-1]
output = ""
for i in range(len(flag)):
    output += chr(ord(flag[i]) + 1)
print(output)

# Stuff to translate into js
output = ">>RgBOE[y9G[BK3YB:2dy9m[{q3YpSYN4:mdmiHe{dHN1:mcwGEeBO3d2[HOjC{fnS4Z1O4d"
test = ""
for i in range(len(output)):
    test += chr(ord(output[i]) - 1)
test = test[::-1]
test = base64.b64decode(test.encode()).decode()

print(test)