from tkinter import *
import sqlite3 as sql

con = sql.connect('chipi.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS fullname(id INTEGER PRIMARY KEY, lastname TEXT, firstname TEXT)')
con.commit()


def sudo_heck_write(event):
    cur.execute('INSERT INTO fullname(lastname, firstname) VALUES(?,?)', (strF.get(), strF2.get()))
    con.commit()

frame = Frame()
labelF = Label(text='Фамилия')
labelF.grid(column=0, row=0)

strF = StringVar()
editF = Entry(textvariable=strF)
editF.grid(column=0, row=1)

labelF2 = Label(text='Имя')
labelF2.grid(column=0, row=2)

strF2 = StringVar()
editF2 = Entry(textvariable=strF2)
editF2.grid(column=0, row=3)

labelF3 = Label(text='Возраст')
labelF3.grid(column=0, row=4)

strF3 = IntVar()
editF3 = Entry(textvariable=strF3)
editF3.grid(column=0, row=5)

bts = Button(text='Записать')
bts.bind('<Button-1>', sudo_heck_write)
bts.grid(column=0, row=6)

frame.mainloop()
