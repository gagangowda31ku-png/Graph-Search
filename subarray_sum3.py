def subarray_sum2(arr ,target):
    n = len(arr)
    i , j , s = 0 , 0 , 0
    while i < n and j < n+1:
        if s == target:
            return i , j
        elif s < target:
            if j < n:
                s += arr[j]
                j+=1

        elif s > target:
            s -= arr[i]
            i += 1
arr = [1,5,8,0,5,3,8,9]
target = 18    

print(subarray_sum2(arr , target))
