from random import shuffle

flag = 'sstctf{fl1pp1ng_l1s+s_al1_d4y_3very_day!}'

sorted = [i for i in range(1,8)]
shuffled = list(sorted)

def pivot(arr,idx):
        global tries
        tries += 1
        return arr[idx+1:]+[arr[idx]]+arr[:idx]

def pivot_sort(arr):
    for i in range(len(arr),0,-1):
        if i == len(arr):
            pass
        else:
            arr = pivot(arr,arr.index(i))
        if arr == sorted:
            return arr
        if arr.index(i) != 0:
            arr = pivot(arr,arr.index(i)-1)
        if arr == sorted:
            return arr
    return arr

# just to ensure the user doesn't get too easy of a list
while True:    
    shuffle(shuffled)
    tries = 0

    pivot_sort(shuffled)
    if tries >= 11 and shuffled != sorted:
        break

print('Welcome to list flipping simulator! Your goal is to sort the list.')
for i in range(11,0,-1):
    print('List:')
    print(shuffled)
    print(f'You have {i} chances left to flip.')
    idx = int(input('Enter the index which you would like to flip around: '))
    shuffled = pivot(shuffled,idx)
    print()

    if shuffled == sorted:
        print('Congratulations! Here\'s your flag:')
        print(flag)
        exit()

print('You ran out of chances! Better luck next time!')