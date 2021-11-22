def sorted(x) :
    y = list(x)
    for last in range(len(y)-1,-1,-1) :
        swapped = False
        for i in range(last) :
            if y[i] > y[i+1] :
                y[i], y[i+1] = y[i+1], y[i]
                swapped = True
        if not swapped :
            break
    if x == y :
        return True
    else :
        return False

inp = [int(i) for i in input('Enter Input : ').split()]
if sorted(inp) :
    print("Yes")
else :
    print("No")