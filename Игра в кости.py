from tkinter import *
import random, time

def brosok():
    x = random.choice(['1.png','2.png','3.png',
                       '4.png','5.png','6.png',])
    return x

def img(event):
    global b1,b2
    for i in range(10):
        b1 = PhotoImage(file=(brosok()))
        b2 = PhotoImage(file=(brosok()))
        lab1['image'] = b1
        lab2['image'] = b2
        time.sleep(0.2)
    

root = Tk()
root.geometry('800x640')
root.title('Бросок костей')
root.resizable(height = False, width = False)
root.iconphoto(True, PhotoImage(file=('brjyrf.png')))
font = PhotoImage(file=('трава.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab2 = Label(root)
lab1.place(relx=0.2, rely=0.5, anchor= CENTER)
lab2.place(relx=0.7, rely=0.5, anchor= CENTER)
root.bind('<1>', img)
root.mainloop()
