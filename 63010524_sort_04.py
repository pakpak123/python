lst = [str(i) for i in input('Enter Input : ').split()]


for loop in range(len(lst)):
    maxIndex = 0
    maxAlphabet = ''
    for i in range(len(lst)-loop):              
        for ele in lst[i]:
            if 'a' <= ele <= 'z':
                if i == 0:
                    maxAlphabet = ele
                else:
                    if ele > maxAlphabet:
                        maxAlphabet = ele
                        maxIndex = i
                        
    lst[len(lst)-loop-1], lst[maxIndex] = lst[maxIndex], lst[len(lst)-loop-1]

print(' '.join(lst))