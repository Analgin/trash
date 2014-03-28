#-*-coding:utf-8-*

"""
                                    -----------------------------------------------------
                                    |                       Creared                      |
                                    |                                                    |
                                    |                 Analgin[Dobro]                     |
                                    |                                                    |
                                    |                                                    |
                                     -----------------------------------------------------                                                                       

"""



import re

import os

import time

import tkinter

from tkinter import *

from tkinter.filedialog import *

from tkinter.messagebox import *


class Glob:

    flag = 0

win = Tk()

im=PhotoImage(file='icon.gif')

win.iconphoto(True,im)

win.geometry("140x30+-110+0")

win.overrideredirect(1)

win.wm_attributes('-alpha',0.8)

bg = PhotoImage(file='bg.gif')

fo = PhotoImage(file='fo.gif')

act = PhotoImage(file='act.gif')

ex = PhotoImage(file='ex.gif')

op_cl = PhotoImage(file='opcl.gif')

background = Label(win,image=bg)

background.pack()
    

bt_open = Button(win,image = fo)

bt_act = Button(win,image = act)

bt_exit = Button(win,image = ex)

bt_opcl = Button(win,image = op_cl,bd=0)


bt_open.place(x=5,y=4)

bt_act.place(x=35,y=4)

bt_exit.place(x=65,y=4)

bt_opcl.place(x=110,y=0)



def _winopcl(event):

    if Glob.flag == 0:

        i = -110

        while i<0:

            win.geometry("140x30+%s+0"%i)

            win.update()

            i = i+1

        Glob.flag = 1

    else:

        i = 0

        while i>-110:

            win.geometry("140x30+%s+0"%i)

            win.update()

            i = i-1

        Glob.flag = 0

        

def _open(event):

    Glob.text = []

    Glob.file = askopenfilename()

    ll = open(str(Glob.file))

    tl = len(ll.read())

    if tl<90:

        showinfo(title='Стоп!',message='Файл не нуждается в изменении!')

        _winopcl(Event)

        return

    f = open(str(Glob.file))

    Glob.res = {}

    i = 1

    
    for a in f.readlines():

        Glob.res[i] = a.replace(a[:90],a[:90]+'\n')

        i = i+1



def _act(event):
   
    f = open(str(Glob.file),'w+')

    f.close()

    i = 1

    while i<len(Glob.res)+1:

        f = open(str(Glob.file),'a+')

        f.write(str(Glob.res[i]))

        f.close()

        i = i+1

    showinfo(title='Успешно',message='Завершено!',icon='info')


def _exit(event):

    if askyesno(title='Подтверждение',message='Выйти?',icon='question'):

        win.destroy()
        

bt_opcl.bind("<Button-1>",_winopcl)

bt_open.bind("<Button-1>",_open)

bt_act.bind("<Button-1>",_act)

bt_exit.bind("<Button-1>",_exit)

win.mainloop()
