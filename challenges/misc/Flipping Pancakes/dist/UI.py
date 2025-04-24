from random import shuffle

flag = 'sstctf{REDACTED}'

sorted = [i for i in range(1,8)]
shuffled = list(sorted)
shuffle(shuffled)

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