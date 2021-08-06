import random

# random.randint() สุ่มจำนวนเต็ม(min,max)
Better = random.randint(50,100)
print(Better)

# random.uniform() สุ่มเลขทศนิยม
Go = random.uniform(80,100)
print(Go)

# random.choice() เป็นคำสั่ง random จาก List
A = [10,20,30,40]
B = random.choice(A)
print(B)

# random.shuffle() เป็นการสลับตำแหน่งของข้อมูลภายในList
money = [100,500,850,400]
random.shuffle(money)
print(money)

