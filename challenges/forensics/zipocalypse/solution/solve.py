import zipfile
import io
from time import time

start = time()

with open("layer20000.zip", "rb") as f:
    file_bytes = f.read()

while True: # takes a REALLY long time
    try:
        zfile = zipfile.ZipFile(io.BytesIO(file_bytes), "r")
        file_bytes = zfile.read(zfile.infolist()[0])
    except zipfile.BadZipFile:
        print(file_bytes)
        duration = int(time()-start)
        sec = duration % 60
        min = duration // 60
        print('Time elapsed:',min,'min',sec,'sec')
        break
