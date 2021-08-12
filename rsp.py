from tkinter import *
from PIL import Image,ImageTk
import random
page=Tk()
list1=['stone','paper','scissor']
def click(event):
    option=event.widget.cget('text')
    random_choice=random.choice(list1)
    if option=='stone':
        if random_choice=='stone':
            l1.config(text='Tie...!both have point..!',bg='black',fg='red')
        elif random_choice=='paper':
            l1.config(text='Paper cover rock! you lose..!',bg='black',fg='red')
        elif random_choice=='scissor':
            l1.config(text='Rock smash scissor! you win..!',bg='wheat',fg='black')
    if option=='paper':
        if random_choice=='paper':
            l1.config(text='Tie..!both have point..!',bg='black',fg='red')
        elif random_choice == 'stone':
            l1.config(text='Paper cover rock! you win..!',bg='wheat',fg='black')
        elif random_choice == 'scissor':
            l1.config(text='Scissor cuts paper! you lose..!',bg='black',fg='red')
    if option=='scissor':
        if random_choice=='scissor':
            l1.config(text='Tie..!both have point..!',bg='black',fg='red')
        elif random_choice == 'paper':
            l1.config(text='Scissor cuts paper! you win..!',bg='wheat',fg='black')
        elif random_choice == 'stone':
            l1.config(text='Rock smash scissor! you lose..!',bg='black',fg='red')

if __name__ == '__main__':
    page.title('rs')
    page.geometry('500x500')
    page.config(bd=1,bg='white')
    i1=Image.open(r'H:\python_project\stone.jpg')
    i2=Image.open(r'H:\python_project\paper.jpg')
    i3=Image.open(r'H:\python_project\scissor.jpg')
    S=ImageTk.PhotoImage(i1)
    P=ImageTk.PhotoImage(i2)
    Sc=ImageTk.PhotoImage(i3)
    btn1=Button(page,text='stone',image=S,bd=10,relief=GROOVE)
    btn1.place(x=0,y=370)
    btn2=Button(page,text='paper',image=P,bd=10,relief=GROOVE)
    btn2.place(x=0,y=0)
    btn3=Button(page,text='scissor',image=Sc,bd=10,relief=GROOVE)
    btn3.place(x=350,y=0)
    btn1.bind('<Button-1>',click)
    btn2.bind('<Button-1>',click)
    btn3.bind('<Button-1>',click)
    l1=Label(page,font="Helvetica 36 bold",fg='black')
    l1.place(x=500,y=600)
    l2=Label(page,text='Your result',font="Helvetica 36 bold",fg='black')
    l2.place(x=650,y=500)
    page.mainloop()