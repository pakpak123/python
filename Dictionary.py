# Dictionary คือการเพิ่มชนิดของข้อความเยอะๆ
# โดยเรียกเป็นชนิดออกมาแทน index
book ={
    'name': 'Power' ,
    'price' : 120 ,
    'page' : 310
}
print(book)
# การเปลี่ยนชื่อในชนิดข้อมูลทำง่ายๆ
book['name'] = 'Hoshi'
print(book['name'])
# การเพิ่มข้อมูลก็เช่นกันเพิ่มง่ายมาก
book['state'] = 'Korea'
print(book)
# ถ้าจะลบใช้คำสั่ง .pop('ชื่อชนิดข้อมูล')
book.pop('page')
print(book)
