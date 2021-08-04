import tkinter as tk


def show_output():
    number = int(number_input.get())

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number*i) + '\n'
    output_label.configure(text=output)


window = tk.Tk()
window.title('สูครคูณ')
window.minsize(width=400, height=400)
title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack(pady=20)

number_input = tk.Entry(master=window)
number_input.pack()

ok_button = tk.Button(master=window, text='ได้แก่', command=show_output)
ok_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()
