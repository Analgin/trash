#-*-coding:utf-8-*

import os

import html.parser

import urllib

from urllib.request import *

import tkinter

from tkinter import *


#_________________________________________________________________________________| the end import |__________________________________________________________________________________________#

WORK_PATH=os.path.abspath(os.path.normpath(os.getcwd()))



class G:a=0     #-----| for the globalisation variables |-----#

G.root=Tk() #main window

G.root.title('Парсер')

G.root.wm_attributes('-alpha',0.9)

G.root['bg']='#222222'

G.root.minsize(400,200)

G.root.maxsize(400,200)

G.url=Entry(G.root,width=20)

G.url.focus()

re=Label(G.root,fg='white',font=('Segoe Print Bold',10,'bold'),text='url',bg='#222222')

sub=Button(G.root,fg='white',bg='black',font=('Segoe Print Bold',8,'bold'),text='Парсить')

cl=Button(G.root,fg='white',bg='black',font=('Segoe Print Bold',8,'bold'),text='Очистить')

sb=Scrollbar(G.root,width='8',orient=VERTICAL,troughcolor='green')

G.text=Text(G.root,yscrollcommand=sb.set,width='48',height='15',fg='white',bg='#222222',font=('Segoe Print Bold',8),border=0)

sb.config(command=G.text.yview)

#________________________________________________________________________________| placing block |____________________________________________________________________________________________#


G.url.place(x=30,y=10)

re.place(x=0,y=6)

sub.place(x=180,y=5)

cl.place(x=240,y=5)

sb.place(x='395',y='80')

G.text.place(x='1',y='50')

#________________________________________________________________________________| FUNCTIONS |________________________________________________________________________________________________# 


def parseUserQuery(event): #parsing functions

    address='http://'+G.url.get().replace('http:\\','')

    port='80'

    try:

        G.text.insert(END,'Попытка подключения..\n')

        G.root.update()

        Url=urllib.request

        connect=Url.urlopen(address)

    except ValueError:

        G.text.insert(END,'Не верный адрес | '+address+' |\n')

        return

    except ConnectionError:

        G.text.insert(END,'Не удалось подключиться\n')

        return

    except Url.URLError:

        G.text.insert(END,'Невозможно подключиться\n')

        return

    G.text.insert(END,'Соединено!\n')

    G.root.update()

    import re
    
    res=connect.read().decode('utf8')

    patt=r'href=([\'"]*)(\S+)\1'

    out=str(re.findall(patt,res))

    out2=str(re.findall(patt,out))

    rq=html.parser.HTMLParser().unescape(re.findall(patt,res))


    result=str(rq).replace("('",'\n').replace('\"\',','').replace("'",'').replace('),','\n').replace(')','').replace('\n\n','\n').replace('[','').replace(']','')

    
    if not os.path.exists(os.path.join(WORK_PATH+'\ART_parse',str(address).replace('http://','').replace('.','_').replace('/','_')+str('.parse.txt'))):

        try:

            os.mkdir(os.path.join(WORK_PATH,'ART_parse'))

        except:

            a=1

        ff=open(os.path.join(WORK_PATH+'\ART_parse',str(address).replace('http://','').replace('.','_').replace('/','_')+str('.parse.txt')),'w+')

        ff.write(str(result))

        ff.close()

    G.text.insert(END,'\nВыполнено!\n')

    G.root.update()
    


def clear(event):

    G.text.delete(0.1,END)


#_______________________________________________________________________________| BINDS |_____________________________________________________________________________________________________#



sub.bind('<Button-1>',parseUserQuery)

cl.bind('<Button-1>',clear)


#__________________________________________________________________________________END________________________________________________________________________________________________________#


G.root.mainloop()
