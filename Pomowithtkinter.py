# Pomodoro TImer

import time
import datetime as dt
import tkinter
from tkinter import messagebox
import winsound

now = dt.datetime.now()
pom = 25*60
delta = dt.timedelta(0,pom)
fut = now + delta
sec = 5*60
fin = now + dt.timedelta(0, pom + sec)

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Pomo has Started!!", '\nIt is now ' + now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins. ")

pomodoros = 0
breaks = 0

while True:

    if now < fut:
        print('pomodoro')
    elif fut <= now <= fin:
        print('in break')
        if breaks  == 0:
            print('in break')
            for i in range(5):
                winsound.Beep((i + 100), 700)
            print('Break time!')
            breaks += 1
    else:
        print('finished')

        breaks = 0
        for i in range(10):
            winsound.Beep((i + 100), 500)

        ans = messagebox.askyesno("Promo is Finished!","Would you like to start another pomo?")
        pomodoros += 1
        if ans == True :
            now = dt.datetime.now()
            fut = now + dt.timedelta(0, pom)
            fin = now + dt.timedelta(0, pom + sec)
            continue
        elif ans == False:

            messagebox.showinfo("Pomod FInished!!")
            break
    print('sleeping')
    time.sleep(20)
    now = dt.datetime.now()
    timenow = now.strftime("%H:%M")

