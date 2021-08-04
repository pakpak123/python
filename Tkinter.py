import tkinter as tk
# tkinter = การสร้างแอปแบบง่ายๆ ข้อความ กรอบ ปุ่ม

def set_message():
    text = text_input.get()
    title_label.configure(text=text)


window = tk.Tk()
window.title('Nuest')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='เมื่อรักฉันเกิด')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='ok',command=set_message )
ok_button.pack()

window.mainloop()
