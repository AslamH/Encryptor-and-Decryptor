from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
import os
import smtplib

root=Tk(className='      AEDP      ')
root.geometry('650x650')

def getmsg():
    window=Tk(className='Mailing')
    window.geometry('650x200')
    framem=Frame(window)
    framem.pack()
    label=Label(framem,font='Ariel',text='Enter receiver mail address:')
    label.pack(side=TOP)
    email1=Entry(framem,width=80)
    email1.pack()

    framem2=Frame(window)
    framem2.pack()
    label1=Label(framem2,font='Ariel',text='Enter subject:')
    label1.pack(side=TOP)
    emailad=Entry(framem2,width=80)
    emailad.pack()

    framem1=Frame(window)
    framem1.pack()
    but=Button(framem1,command=send_mail,bg='pink',font='Ariel',text='send',width=10,height=2,bd=4)
    but.pack()

    window.mainloop()


def send_mail():
    s=smtplib.SMTP('localhost')

    #email1.focus_set()
    to=email1.get()

    msg=e9.insert(END,(encrypt(a,b)))

    #from:'aslamhussein8@gmail.com'

    e1.focus_set()
    #subject:emailad.get()
    s.sendmail('aslamhussein8@gmail.com',to,msg)
    s.quit()

def lnupdater(event = None):
    el, ec = e9.index('end-1c').split('.')
    cl, cc = e9.index('insert').split('.')

def open_command(event = None):
        filename=askopenfilename(parent = root,title = 'Select a file')
        if filename != None:
                fo = open(filename,mode = 'r')
                contents = fo.read()
                e9.delete('1.0',END)
                e9.insert('1.0',contents)
                fo.close()
                root.title(os.path.basename(filename))
                lnupdater()


def save_command(event = None):
    filename = asksaveasfilename(parent =root,filetypes=[('Text', '*.txt')],title = 'Save file as')
    if filename is not None:
            file = open(filename,mode = 'w')
            data = e9.get('1.0',END)
            file.write(data)
            file.close()
            lnupdater()


def wordlist(a):
    word_list=(list(a))
    return (word_list)

def length(a):
    return(len(wordlist(a))-1)

def encrypt(a,b):
    thelist=wordlist(a)
    for j in range (0,length(a)+1):
        thelist[j]=(chr(ord(wordlist(a)[j])+(b)))
        j=j+1
    return (''.join(thelist))

def callback():
    e9.focus_set()
    a=e9.get("1.0",'end-1c')

    e1.focus_set()
    b=int(e1.get())

    e9.delete(1.0,END)
    e9.insert(END,(encrypt(a,b)))

def copy_command(event = None):
    root.clipboard_clear()
    lnupdater()

def paste_command(event = None):
    text = e9.selection_get(selection = 'CLIPBOARD')
    e9.insert(INSERT,text)
    lnupdater()
def exit_command(event = None):
    result = askquestion("Exit", "Are You Sure?", icon = 'warning')
    if result == 'yes':
        root.destroy()




frame9=Frame(root)
frame9.pack()
label1=Label(frame9,text='Enter Text:',font='Ariel',bd=6,fg='red4')
label1.pack(side=TOP)
label9=Button(frame9,fg='red4',bd=6,text='Upload:',font='Ariel',command=open_command,activebackground='red4')
label9.pack(side=BOTTOM)
e9=Text(frame9,font='Ariel',width=42,height=20)
e9.pack(side=RIGHT)

text = e9.get("1.0",'end-1c')

frame0 = Frame(root)
frame0.pack()
label1=Label(frame0,text='Encryption Key:',font='Ariel',bd=6,fg='red4')
label1.pack(side=LEFT)
e1=Entry(frame0,font='Ariel',width=30)
e1.config(show='*')
e1.pack(side=RIGHT)



frame1 = Frame(root)
frame1.pack()
label2=Button(frame1,text='Encrypt:',command=callback,font='Ariel',bd=6,fg='red4',activebackground='red4')
label2.pack(side=TOP)

framex= Frame(root)
framex.pack()
labelx=Label(framex,text='Decryption Key:',font='Ariel',bd=6,fg='red4')
labelx.pack(side=LEFT)
ex=Entry(framex,font='Ariel',width=30)
ex.config(show='*')
ex.pack(side=RIGHT)

def newlist(x):
    real=list(x)
    return (real)

def newlength(x):
    return(len(newlist(x))-1)

def decrypt(x,c):
    delist= newlist(x)
    j=0
    while j<=(newlength(x)):
        delist[j]=(chr(ord(newlist(x)[j])-(c)))
        j=j+1
    return (''.join(delist))


def bringit():
    e9.focus_set()
    x=e9.get("1.0",'end-1c')

    ex.focus_set()
    c=int(ex.get())

    e9.delete(1.0,END)
    e9.insert(END,(decrypt(x,c)))

def about():
    window=Tk(className='    About AEDP   ')
    window.geometry('500x400')
    frame=Frame(window,width=500,height=400,bg='pink')
    label1=Label(frame,bg='pink',font='Ariel',text='This is version 1.1 of the AEDP.')
    label=Label(frame,bg='pink',font='Ariel',text='This is a simple application for encrypting and decrypting text.\n Hope you enjoy using it.')
    label1.place(x=0,y=25)
    label.place(x=0,y=50)
    x=Label(frame,text='© 2016 production',bg='pink',font='Ariel')
    x.place(x=200,y=370)
    frame.pack()
    window.mainloop()

framey = Frame(root)
framey.pack()
label1=Button(framey,text='Decrypt:',command=bringit,font='Ariel',bd=6,fg='red4',activebackground='red4')
label1.pack(side=BOTTOM)


menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File",font='Ariel', menu=filemenu)
filemenu.add_command(label="New",accelerator = "Ctrl+N")
filemenu.add_command(label="Open",command=open_command,accelerator = "Ctrl+O")
filemenu.add_command(label="Save",command=lambda :save(root,text),accelerator = "Ctrl+S")
filemenu.add_command(label='Send encrypted document as email',command=getmsg,accelerator = "Ctrl+E")
filemenu.add_command(label='Send decrypted document as email',accelerator = "Ctrl+D")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit_command,accelerator = "Ctrl+Q")

editmenu=Menu(menu)
menu.add_cascade(label="Edit",font='Ariel', menu=editmenu)
editmenu.add_command(label="Copy",command=copy_command,accelerator = "Ctrl+C")
editmenu.add_command(label="Paste",command=paste_command,accelerator = "Ctrl+P")

helpmenu = Menu(menu)
menu.add_cascade(label="Help",font='Ariel', menu=helpmenu)
helpmenu.add_command(label="About  AEDP",command=about)
helpmenu.add_command(label="Check For Updates")

root.bind('<Control-n>')
root.bind('<Control-o>', open_command)
root.bind('<Control-q>', exit_command)
root.bind('<Control-c>', copy_command)
root.bind('<Control-p>', paste_command)
root.bind('<Control-s>', save_command)
root.bind('<Control-e>')
root.bind('<Control-d>')

root.mainloop()

