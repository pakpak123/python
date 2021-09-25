# class คือคำสั่งที่ประกาศออกมาก่อนแล้ว เหมือนโรงงานผลิตรถยนต์ ส่วนรถยนต์เป็นobjectที่อยู่ในclass อีกที
class Tank:
    def __init__(self,name,ammo):
        self.name=name
        self.ammo=ammo
    def size(self):
        return len(self.name)


first_tank = Tank('Rose',3)
# อยากเพิ่มกระสุนเป็น 5 จะตั้งค่าให้เป็น =5 หรือ+=2 ก็ได้
first_tank.ammo+=2
print(first_tank.ammo)
print(first_tank.size())

second_tank = Tank('Great',7)
second_tank.ammo=9
print(second_tank.name)
print(second_tank.ammo)



