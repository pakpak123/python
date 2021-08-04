# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# การกำหนดตัวแปลทำได้ง่ายๆไม่ต้องเลือกประเภทเหมือน ภาษาซี
x = 18
# แสดงผลทำง่ายๆแค่คำสั่ง print()
print(x)
# if ก็ไม่ต่างกับภาษาซีกำหนดเงื่อนไขแล้วอย่าลืมใส่ : นะ
if x > 10:
    print('A')
elif x != 5:
    print('C')
else:
    print('B')
# คำสั่ง for จะเพิ่มคำว่า in range () เข้าไปด้วยเสมอนับจาก 0 เสมอ
for i in range (1,5):
    if i % 3 ==0:
        continue
    print(i)