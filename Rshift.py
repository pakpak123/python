def Rshift(num,shift):
    return num >> shift

n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))
print(type(n))

""">> คือ Rshift แปลงเลขฐาน 10 ไปเป็นฐาน 2 แล้วก็ไล่ไปทางขวาตามบิตที่ต้องการ พอทำเสร็จจะเป้นการแปลงกลับไปฐาน 10 ให้อัตโนมัติ
 ( Signed right shift ) จะนำค่าของตัวแปรที่อยู่ด้านหน้าเครื่องหมายมาแปลงเป็นตัวเลขฐานสอง 
แล้วเลื่อนค่าบิตไปทางขวา ตามจำนวนค่าของตัวแปรที่อยู่ด้านหลังเครื่องหมาย 
เมื่อได้ผลลัพธ์แล้วจึงแปลงกลับเป็นตัวเลขฐานสิบ """

