from tkinter import *
from tkinter import messagebox
import datetime
import pymysql.cursors
from tkinter import scrolledtext
import re
from prettytable import from_db_cursor
from PIL import Image, ImageTk
from PIL import *
from tkinter import filedialog
import tkinter as tk
selim=0
val=0
window = Tk()
window.geometry("700x650")
window.title("Final project")
dd=IntVar(window)
mm=IntVar(window)
yy=IntVar(window)
imgSet = BooleanVar()

#validation with file management system
def validation():
    global selim
    global val
    val = 0
    ch1 = 0
    ch2 = 0
    ch3 = 0
    ch4 = 0

    v1 = entry_1.get()
    v2 = entry_2.get()
    v3 = entry_3.get()
    v4 = entry_4.get()
    v5 = entry_5.get()
    v6 = x1.get()
    v7 = txt.get("1.0", "end-1c")
    v8 = vari.get()

    if(len(v1) != 0 and v1.isalpha() == True):
        if(len(v2) != 0 and v2.isalpha() == True):
            with open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\stdid.txt', 'r')as stdid:
                if v3 in stdid.read():
                    ch1 = 1
                else:
                    ch1 = 0
            if(ch1 == 0 and v3.isdigit() == True):
                with open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\contact.txt', 'r')as contact:
                    if v4 in contact.read():
                        ch2 = 1
                    else:
                        ch2 = 0
                if(len(v4) == 10 and v4.isdigit() == True and ch2 == 0):
                    with open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\email.txt', 'r')as email:
                        if v5 in email.read():
                            ch3 = 1
                        else:
                            ch3 = 0
                    if(ch3 == 0):
                        match = re.search("@gmail.com$", v5)
                        if(match):
                            with open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\roll.txt', 'r')as roll:
                                if v6 in roll.read():
                                    ch4 = 1
                                else:
                                    ch4 = 0
                            if(v6 != 0 and ch4 == 0):
                                if(v7 != 0):
                                    if(v8 != "Select" ):
                                        if(selim):
                                            f = open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\stdid.txt', 'a')
                                            f.write(f'{v3}\n')
                                            f = open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\contact.txt', 'a')
                                            f.write(f'{v4}\n')
                                            f = open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\email.txt', 'a')
                                            f.write(f'{v5}\n')
                                            f = open(r'C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\roll.txt', 'a')
                                            f.write(f'{v6}\n')
                                            f.close()
                                            val = 1
                                        else:
                                            messagebox.showwarning("Error", "Enter a valid image")
                                    else:
                                        messagebox.showwarning(
                                            "Error", "Select Gender")
                                else:
                                    messagebox.showwarning(
                                        "Error", "Enter address")
                            else:
                                if(ch4 == 1):
                                    messagebox.showwarning(
                                        "Error", "Roll no already present")
                                else:
                                    messagebox.showwarning(
                                        "Error", "Enter valid roll no.")
                        else:
                            messagebox.showwarning(
                                "Error", "Enter a valid email")
                    else:
                        messagebox.showwarning(
                            "Error", "Email already present")
                else:
                    if(ch2 == 1):
                        messagebox.showwarning(
                            "Error", "Contact number already present")
                    else:
                        messagebox.showwarning(
                            "Error", "Invalid contact number \n Try Again")
            else:
                messagebox.showwarning("Error", "Enter a valid student ID")

        else:
            messagebox.showwarning("Error", "Enter Last  Name \n Try Again")

    else:
        messagebox.showwarning("Error", "Enter First Name \n Try Again")

    if(val == 1):
        messagebox
        database()
    else:
        messagebox.showwarning("Error", "Please enter proper details")

#database querys
def database():
    global selim
    if(selim):
        d1 = entry_1.get()
        d2 = entry_2.get()
        d3 = entry_3.get()
        d4 = vari.get()
        d5 = w3.get()+'-'+w2.get()+'-'+w1.get()
        d6 = entry_4.get()
        d7 = entry_5.get()
        d8 = x1.get()
        d9 = txt.get("1.0", "end-1c")
        
        #global curs
        
        curs = pymysql.connect(host="localhost", user="root",
                            password="")
        mycursor = curs.cursor()
        mycursor.execute('CREATE DATABASE IF NOT EXISTS management')
        curs.close()
        curs = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='management'
                             )
        mycursor=curs.cursor()
        table = "CREATE TABLE IF NOT EXISTS student(FirstName VARCHAR(255),Lastname VARCHAR(255),StudentID INT,Gender VARCHAR(255),Date DATE,Contact VARCHAR(10),Email VARCHAR(255),Roll INT,Address VARCHAR(255),Photo BLOB)"
        mycursor.execute(table)
        a = "INSERT INTO student(FirstName,Lastname,StudentID,Gender,Date,Contact,Email,Roll,Address,Photo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        image = converttoBinaryData()
        r1 = (d1, d2, d3, d4, d5, d6, d7, d8, d9, image)
        mycursor.execute(a, r1)
        curs.commit()
        curs.close()
    else:
        messagebox.showwarning(
                                "Error", "Enter a valid image")

#converts the image to binary coding
def converttoBinaryData():
    with open("Test.jpg", "rb") as file:
        binaryData = file.read()
    return binaryData

#shows the current record
def printed():
    global selim
    global val
    print(selim)
    if(selim and val):
        win = Tk()
        win.geometry("1000x1000")
        win.configure(bg="white")
        win.title("DISPLAY")
        pathf = "Test.jpg"
        im = Image.open(pathf)
        im = im.resize((150, 150))
        tkimage = ImageTk.PhotoImage(im, master=win)
        profilePhoto = Label(win, image=tkimage)
        profilePhoto.image = tkimage
        profilePhoto.place(x=100, y=50)

        Label(win, text="First Name").place(x=100, y=250)
        Label(win, text="Last Name").place(x=100, y=300)
        Label(win, text="Student ID").place(x=100, y=350)
        Label(win, text="Address").place(x=100, y=400)
        Label(win, text="Mobile No.").place(x=100, y=450)
        Label(win, text="Email").place(x=100, y=500)
        Label(win, text="Roll No.").place(x=100, y=550)
        Label(win, text="Date of Birth").place(x=100, y=600)
        Label(win, text="Gender").place(x=100, y=650)

        Label(win, text=entry_1.get(), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=250)
        Label(win, text=entry_2.get(), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=300)
        Label(win, text=entry_3.get(), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=350)
        Label(win, text=txt.get("1.0", "end-1c"), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=400)
        Label(win, text=entry_4.get(), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=450)
        Label(win, text=entry_5.get(), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=500)
        Label(win, text=x1.get(), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=550)
        Label(win, text=w1.get()+'/' + w2.get()+'/' + w3.get(), bg="white",
            width=50, font="bold", relief="raised").place(x=250, y=600)
        Label(win, text=vari.get(), bg="white", width=50,
            font="bold", relief="raised").place(x=250, y=650)
    else:
        messagebox.showwarning(
                                "Error", "Enter all details")

#sets the selected image
def selImage():
    global selim
    path = filedialog.askopenfilename(parent=window, title='Choose file', filetypes=[
                                      ("Image File", '.jpg'), ("png Images", ".png")])
    im = Image.open(path)
    im = im.resize((150, 150))
    tkimage = ImageTk.PhotoImage(im)
    im.save("Test.jpg")
    imgholder.config(image=tkimage)
    imgholder.image = tkimage
    imgSet.set(True)
    selim=1
    print(selim)

#clears the current record
def clear():
    dd=IntVar(window)
    mm=IntVar(window)
    yy=IntVar(window)
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    vari.set("select")
    dd.set(1)
    w1.config(textvariable=dd)
    mm.set(1)
    w2.config(textvariable=mm)
    yy.set(1980)
    w3.config(textvariable=yy)
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')
    x1.delete(0, 'end')
    txt.delete('1.0', 'end')
    global selim
    selim=0
    im = Image.open(r"C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\sampleimg.png")
    im = im.resize((150, 150))
    tkimage = ImageTk.PhotoImage(im)
    im.save("sample.png")
    imgholder.config(image=tkimage)
    imgholder.image = tkimage
    imgSet.set(True)

#show all records from database
def showall():
    win=Tk()
    win.geometry('1000x1000')
    win.configure(bg="white")
    win.title("DISPLAY")
    entry=Text(win)
    entry.place(x=0,y=0,width=1000,height=500)
    curs=pymysql.connect(host="localhost",user="root",password="",db="management")
    mycursor=curs.cursor()
    mycursor.execute("SELECT FirstName,Lastname,StudentID,Gender,Date,Contact,Email,Roll,Address FROM student ")
    x=from_db_cursor(mycursor)
    entry.insert(INSERT,x)

# all labels and buttons
label = Label(window, text="STUDENT MANAGEMENT SYSTEM",
              relief="raised", fg="White", width=50, font="bold", bg="#4089ff")
label.place(x=40, y=10)
label1 = Label(window, text=" First Name :", relief="raised",
               width=10, fg="black", font="bold", bg="white")
label1.place(x=5, y=50)

entry_1 = Entry(window, width=40, relief="solid", font = "Helvetica 12")
entry_1.place(x=130, y=51,height=27)

label2 = Label(window, text=" Last Name :", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label2.place(x=5, y=90)

entry_2 = Entry(window, width=40, relief="solid", font = "Helvetica 12")
entry_2.place(x=130, y=91,height=27)

label3 = Label(window, text=" Student ID :", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label3.place(x=5, y=130)

entry_3 = Entry(window, width=40, relief="solid", font = "Helvetica 12")
entry_3.place(x=130, y=131,height=27)

label4 = Label(window, text="Gender :", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label4.place(x=5, y=170)

choices = ["Male", "Female"]

vari = StringVar(window)
vari.set("Select")
g = OptionMenu(window, vari, *choices)
g.place(x=130, y=170)
dlabel=Label(window,text="(DD-MM-YYYY)",fg="black", width=12,font="Helvetica 10" ,bg="white")
dlabel.place(x=300,y=210)
label5 = Label(window, text="Date of birth:", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label5.place(x=5, y=210)
w1 = Spinbox(window, from_=1, to=31, width=5,textvariable=dd)
w1.place(x=130, y=210,height=27)
w2 = Spinbox(window, from_=1, to=12, width=5,textvariable=mm)
w2.place(x=190, y=210,height=27)
w3 = Spinbox(window, from_=1980, to=2019, width=5,textvariable=yy)
w3.place(x=250, y=210,height=27)
label6 = Label(window, text=" Contact :", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label6.place(x=5, y=250)
entry_4 = Entry(window, width=40, relief="solid", font = "Helvetica 12")
entry_4.place(x=130, y=251,height=27)
label7 = Label(window, text="Email :", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label7.place(x=5, y=290)
entry_5 = Entry(window, width=40, relief="solid", font = "Helvetica 12")
entry_5.place(x=130, y=291,height=27)
label8 = Label(window, text=" Roll no. :", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label8.place(x=5, y=330)
x1 = Entry(window, width=40, relief="solid", font = "Helvetica 12")
x1.place(x=130, y=330,height=27)
label9 = Label(window, text=" Address :", relief="raised",
               fg="black", width=10, font="bold", bg="white")
label9.place(x=5, y=370)
txt = Text(window, height=5, width=60, relief="solid", font = "Helvetica 12")
txt.place(x=130, y=372)
b1 = Button(window, text="Enter", width=12, relief="raised",
            font="bold", bg="#04b834", fg="white", command=validation)
b1.place(x=400, y=530)
b2 = Button(window, text="Show", width=12, relief="raised",
            font="bold", bg="#04b834", fg="white", command=printed)
b2.place(x=250, y=530)
b3 = Button(window, text="Clear", width=12, relief="raised",
            font="bold", bg="#FF2E2E", fg="white", command=clear)
b3.place(x=100, y=530)
b4 = Button(window, text="Show All", width=12, relief="raised",
            font="bold", bg="#04b834", fg="white", command=showall)
b4.place(x=250, y=580)
# select Image Button
I1 = Button(window, text="Upload Your Picture", width=16,
            bg="#04b834", fg="white", command=selImage)
I1.place(x=550, y=50)
# Add path of your sample image below in place of path
Img = Image.open(r"C:\Users\dhuma\Desktop\from pd\Folders\Dnyanesh\sampleimg.png")
sample = Img.resize((150,150))
sampleimg = ImageTk.PhotoImage(sample)
imgholder = Label(window, bg="white", image=sampleimg)
imgholder.place(x=535, y=75)
window.config(bg="white")
window.mainloop()
