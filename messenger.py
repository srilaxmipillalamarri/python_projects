from tkinter import *
import pyautogui as pag
from threading import *
import time


mw = Tk()
mw.title('auto messenger')
mw.iconbitmap('image/messenger.ico')

def justcheck(check):
    if check:
        send_btn.config(text='Running...',state='disabled')
    else:
        send_btn.config(text='Start sending...', state='normal')

class AutoMessenger(Thread):
    hmt_c=5
    wt_c=3
    msg_c='Runninng'


    def run(self):
        justcheck(True)
        i=1
        while True:
            time.sleep(self.wt_c)
            pag.typewrite(self.msg_c)
            pag.press('enter')
            if self.hmt_c==i:
                justcheck(False)
                break
            i +=1

def messenger(hmt, wt, msg):
    print(hmt, 'times')
    print(wt, 'seconds')
    print(msg)
    send = AutoMessenger()
    send.hmt_c=int(hmt)
    send.wt_c=float(wt)
    send.msg_c=msg
    send.daemon = True
    send.start()


# creating widgets

hmt_label = Label(mw, text='How many times:', font=('Arial', 14))
hmt_e = Entry(mw, width=5, font=('Arial', 18))
hmt_times = Label(mw, text='times(0 to infinite times)', font=('Arial', 12))

wt_e = Entry(mw, width=5, font=('Arial', 18))
wt_label = Label(mw, text='Waiting time:', font=('Arial', 14))
wt_sec = Label(mw, text='seconds', font=('Arial', 12))

msg_label = Label(mw, text='messege:', font=('Arial', 14))
msg_e = Entry(mw, width=30, font=('Arial', 18))

send_btn = Button(mw, text='Start sending!', font=('Arial', 14),
                  command=lambda: messenger(hmt_e.get(), wt_e.get(), msg_e.get()))

# showing widgets

hmt_label.grid(row=0, column=0, padx=10, pady=15, sticky=E)
hmt_e.grid(row=0, column=1, padx=10, pady=15, sticky=W)
hmt_times.grid(row=0, column=1, padx=85, pady=15, sticky=W)

wt_label.grid(row=1, column=0, padx=10, pady=15, sticky=E)
wt_e.grid(row=1, column=1, padx=10, pady=15, sticky=W)
wt_sec.grid(row=1, column=1, padx=85, pady=15, sticky=W)

msg_label.grid(row=2, column=0, padx=10, pady=15, sticky=E)
msg_e.grid(row=2, column=1, padx=10, pady=15, columnspan=2, sticky=W)

send_btn.grid(row=3, column=1, pady=20)

mw.mainloop()
