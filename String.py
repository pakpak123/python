message = 'Unforgotable Love รักนี้ไม่ลืมเลือน'
# ภาษาไทยวรรณยุกต์นับเป็น 1 ตัวด้วย อีกทั้งช่องว่างก็นับเป็น 1
number = len(message)
print(number)
result = message.replace(' รักนี้ไม่ลืมเลือน','!!!')
print(result)

Apple = '112'
# .isdigit() คือเช็คว่าข้อมูลที่รับมาเป็นตัวเลขหมดเลยไหม
# ถ้าใช่หรือไม่จะแสดงผลเป็นแค่จริงเท็จเท่านั้น
check = Apple.isdigit()
print(check)

animal = 'carot'
rabbit1 = animal.upper() #ตัวใหญ่หมดเลย
rabbit2 = animal.capitalize() # ตัวใหญ่เเค่ตัวแรกที่เหลือตัวเล็ก

print(rabbit1,rabbit2)