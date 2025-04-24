import math

radius = 70
board = [[0]*100 for _ in range(100)]

x,y = [int(x) for x in input('Enter your x and y coordinates for where you want your flag to be, separated by a space: ').split()]
if x > 70 or y > 70:
    print("You're too far away, we are making sure that you don't even reach the edge of our reach!")
    exit()

board[y][x] = 'flag'

if math.sqrt((x-49)**2+(y-49)**2) < radius:
    board[y][x] = 'HAHA WE STOLE YOUR FLAG'

for itm in board:
    if 'flag' in itm:
        from secret import flag
        print('How did you protect your flag so well??')
        print('Anyway, here it is:',flag)
        break
else:
    print('Nice try, your flag is in the radius so the organisers stole it.')