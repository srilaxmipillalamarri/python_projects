from tkinter import *
from tkinter import filedialog
import pywhatkit as kit
from threading import *

mw = Tk()
mw.title('hand writing txt')
mw.geometry('640x200')

filepath = ''


def selectfile():
    global filepath
    filepath = filedialog.askopenfilename(title="open a text file:",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    db.config(state="normal")
    db.delete(0, END)
    db.insert(0, filepath)
    db.config(state="disable")


def convert():
    global filepath
    if filepath != '':
        select_btn.config(state="disabled")
        cvt_btn.config(text="please wait..!", state="disabled")
        lbl.config(text="writing....")
        pngfilename = filepath.replace('.txt', '.png')
        tf = open(filepath, 'r', encoding="utf8")
        text = tf.read()
        kit.text_to_handwriting(string=text, save_to=pngfilename, rgb=(3, 22, 145))
        lbl.config(text="your file is ready", fg="green")
        select_btn.config(state="normal")
        cvt_btn.config(text="please wait..!", state="normal")


def doit():
    t1 = Thread(target=convert)
    t1.daemon = True
    t1.start()


db = Entry(mw, width=30, font=('', 20))
db.grid(row=0, column=0, padx=(20, 10), pady=20)

select_btn = Button(mw, text='Select a file', font=('', 14), command=selectfile)
select_btn.grid(row=0, column=1, padx=(10, 20), pady=20)

cvt_btn = Button(mw, text='Text to hand writing!', font=('', 14), command=convert)
cvt_btn.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

lbl = Label(mw, text='Created by sri', font=('', 16))
lbl.grid(row=2, column=0, padx=20, pady=(10, 20), columnspan=2, sticky=W)

mw.mainloop()
