counter = 0
def mergeSort(ls):
    global counter
    if len(ls) > 1:
        mid = len(ls)//2
        left = ls[:mid]
        right = ls[mid:]
        mergeSort(left)
        mergeSort(right)
        num1, num2, num3 = 0, 0, 0
        while num1 < len(left) and num2 < len(right):
            if left[num1] < right[num2]:
                ls[num3] = left[num1]
                num1 += 1
            else:
                ls[num3] = right[num2]
                num2 += 1
            num3 += 1
            counter += 1
        while num1 < len(left):
            ls[num3] = left[num1]
            num1 += 1
            num3 += 1
        while num2 < len(right):
            ls[num3] = right[num2]
            num2 += 1
            num3 += 1

print(' *** Merge sort ***')
inp = [int(i) for i in input('Enter some numbers : ').split(' ')]
mergeSort(inp)
print("\nSorted -> ", end='')
for i in range(len(inp)):
        print(inp[i], end=" ")
print('\nData comparison = ', counter)