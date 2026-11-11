def subarray_sum1(arr , target):
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i , n+1):
            if s == target:
                return i , j
            elif s > target:
                break
            if j < n:
                s += arr[j]
arr = [1,5,8,0,5,3,8,9]
target = 18               

print(subarray_sum1(arr , target))
