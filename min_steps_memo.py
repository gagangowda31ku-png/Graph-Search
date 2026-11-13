def min_steps(str1 , str2):
    memo = {}
    def recursive(idx1 = 0 , idx2 = 0):
        key = (idx1 , idx2)

        if key in memo:
            return memo[key]

        elif idx1 == len(str1):
            memo[key] = len(str2) - idx2
        
        elif idx2 == len(str2):
            memo[key] = len(str1) - idx1

        elif str1[idx1] == str2[idx2]:
            memo[key] = recursive(idx1+1 , idx2+1)
        
        else:
            memo[key] = 1 + min(
                recursive(idx1+1 , idx2) ,
                recursive(idx1+1 , idx2+1),
                recursive(idx1 , idx2+1))

        return memo[key]
    return recursive(idx1 = 0 , idx2 = 0)

str1 = 'saturday'
str2 = 'sunday'
print(min_steps(str1 , str2))
