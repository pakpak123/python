def insert(result:list,li:list,n):
    if len(li) == 0:
        return result
    if len(result) == 0:
        result.append(li.pop(0))
        result = insert(result,li,n+1)
    else:
        # print(result)
        if li[0] < result[n-1] and n > 0:
            result = insert(result,li,n-1)
        else:
            temp = li[0]
            result.insert(n,li.pop(0))
            if len(li) == 0:
                print("insert {} at index {} : {}".format(temp,n,result))
            else:
                print("insert {} at index {} : {} {}".format(temp,n,result,li))
            result = insert(result,li,len(result))
    return result


inp = [int(i) for i in input("Enter Input : ").split()]
s = insert([],inp,0)
print("sorted")
print(s)
