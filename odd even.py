def odd_even(data, pos):
    listAns = []
    if pos == 'Odd':
        for i in range(0, len(data)):
            if i % 2 == 0:
                listAns.append(data[i])
    if pos == 'Even':
        for i in range(0, len(data)):
            if i % 2 == 1:
                listAns.append(data[i])
    return listAns


print("*** Odd Even ***")
type_,data,pos = input('Enter Input : ').split(',')
thisList = []
data = str(data)
if type_ == 'S':
    for i in range(0, len(data)):
        thisList.append(data[i])
if type_ == 'L':
    thisList = data.split(' ')
listAns = odd_even(thisList, pos)
if type_ == 'S':
    for i in range(0, len(listAns)):
        print(listAns[i], end='')
if type_ == 'L':
    print(listAns)