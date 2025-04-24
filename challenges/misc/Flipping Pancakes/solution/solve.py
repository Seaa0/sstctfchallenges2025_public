def pivot(arr,idx):
    return arr[idx+1:]+[arr[idx]]+arr[:idx]

def pivot_sort(arr): # run pivot based on this
        sorted = list(arr)
        sorted.sort()
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