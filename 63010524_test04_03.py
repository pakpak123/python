count = 0
def bubble_sort(B):
    global count
    for i in range(len(B)) :
        swapped = False
        for j in range(len(B)-i-1) :
            if B[j] > B[j+1] :
                B[j], B[j+1] = B[j+1], B[j]
                swapped = True
            count = count + 1 
        if not swapped:
            break
    return B

print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
bubble_sort(A)
print()
print(A)
print("Data comparison =", count)