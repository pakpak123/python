import datetime as dt
# dt.datatime.now() บอกวันเวลาตอนนี้
day1 = dt.datetime.now()
print(day1)

# dt.datetime() สั่งวันเวลาแบบกำหนดได้
day2 = dt.datetime(year=2020,month=5,day=19)
print(day2)
# ถ้าไม่ได้ระบุเวลาระบบจะตั้งค่าให้เป็นเที่ยงคืนทันที
# dt.timedelta()
days = dt.timedelta(days=25)
day3 = day2 + days
print(day3)

between = day1 - day2
print(between)