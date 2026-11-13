def min_steps(str1 , str2 , idx1 = 0 , idx2=0):

    if idx1 == len(str1):
        return len(str2) - idx2

    elif idx2 == len(str2):
        return len(str1) - idx1

    elif str1[idx1] == str2[idx2]:
        return min_steps(str1 , str2 , idx1+1 , idx2+1)

    else:
        delete = min_steps(str1 , str2 , idx1+1 , idx2)
        swap = min_steps(str1 , str2 , idx1+1 , idx2+1)
        insert = min_steps(str1 , str2 , idx1 , idx2+1)
        return 1 + min(delete , swap , insert)

str1 = 'saturday'
str2 = 'sunday'

print(min_steps(str1 , str2))
