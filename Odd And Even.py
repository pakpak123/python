def odd_even(arr, s):
    num = len(s)
    if num == 3 :
        for i in range (0,len(arr)):
            if i%2==0:
                print(arr[i],end='')
    else:
        for i in range (0,len(arr)):
            if i%2==1:
                print(arr[i],end='')

def odd_even1(arr, l):
    num = len(l)
    data = arr.split(' ')
    data1 = bool(arr.split(' '))
    data2 = []
    if data1 == True:
        if num == 3:
            for i in range(0, len(data)):
                # odd
                if i % 2 == 0:
                   data2.append(data[i])
            print(data2)


        else:
            for i in range(0, len(data)):
                # even
                if i % 2 == 1:
                    data2.append(data[i])
            print(data2)
    else:
        print('['+"'"+arr+"'"+']')


print("*** Odd Even ***")
kind,message,type = input("Enter Input : ").split(',')
message = str(message)
message2 = []
if 'S' in kind:
    odd_even(message, type)
else:

     if message.isdigit() and len(type)==4:
         odd_even1(message, type)
     elif message.isalnum() and len(type)==4:
        print('[]')
     else:
         odd_even1(message, type)
#Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่