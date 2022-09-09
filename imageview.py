from tkinter import *
from PIL import Image, ImageTk
import os

mw = Tk()
mw.title('Imageviewer')

path = 'image'
files_list = os.listdir(path)
# print(files_list)
img_list = []
for f in files_list:
    if 'png' in f or 'jpg' in f:
        img_with_path = path + '/' + f
        img_list.append(img_with_path)
print(img_list)
img = ImageTk.PhotoImage(Image.open(img_list[1]))
img_label = Label(mw, image=img)
img_label.grid(row=0, column=0, columnspan=3)
img_num = 0


def back_func(num):
    global img, img_num
    fwd_btn.config(state='normal')
    img_num = num - 1
    # print(img_num,len(img_list))
    img = ImageTk.PhotoImage(Image.open(img_list[img_num]))
    img_label.config(image=img)
    if len(img_num) == 0:
        back_btn.config(state='disabled')


def fwd_func(num):
    global img, img_num
    fwd_btn.config(state='normal')
    img_num = num + 1
    # print(img_num,len(img_list))
    img = ImageTk.PhotoImage(Image.open(img_list[img_num]))
    img_label.config(image=img)
    if len(img_list) == img_num + 1:
        fwd_btn.config(state='disabled')


back_btn = Button(mw, text='<<', font=('', 20), state='disabled', command=lambda: back_func(img_num))
back_btn.grid(row=1, column=0, padx=10, pady=20, sticky=W)

exit_btn = Button(mw, text='exit', font=('', 20), command=mw.quit)
exit_btn.grid(row=1, column=1, padx=10, pady=20)

fwd_btn = Button(mw, text='>>', font=('', 20), command=lambda: fwd_func(img_num))
fwd_btn.grid(row=1, column=2, padx=10, pady=20, sticky=E)

mw.mainloop()
