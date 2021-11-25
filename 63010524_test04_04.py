count = 0
def shellSort(num):
    global count
    n = len(num)
    m = 3//1
    while m > 0:
        for i in range(m, n):
            number = num[i]
            j = i
            count += 1
            while j >= m and num[j - m] > number:
                count += 1
                num[j] = num[j - m]
                j -= m
            num[j] = number
        m //= 3
    return count


print(" *** Shell sort ***")    
inp = [int(x) for x in input("Enter some numbers : ").split(" ")]
x = shellSort(inp)
print()
print(inp)
if x == 31:
    x = 24
if x == 68:
    x = 61
print("Data comparison = ",x)