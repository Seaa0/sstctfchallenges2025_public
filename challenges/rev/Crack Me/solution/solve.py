key = b"\\RA7U=0" # var_28
encrypted_flag = b"/!5T![K$b3hdNoh?uMdSW!" # var_20
decrypted = b""
for index, i in enumerate(encrypted_flag):
    # xor
    decrypted += bytes([i ^ key[index % len(key)]])

print(decrypted)