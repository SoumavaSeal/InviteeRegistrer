import tkinter as tk
import dbConnection
import functions

dbConnection.conector()


def homeWindow():
    def add():
        functions.add()

    def show(a):
        functions.show(window, a)

    def updatedView():
        cursor = dbConnection.conn.cursor()
        cursor.execute('select * from invitee')
        window.destroy()
        homeWindow()

    def search():
        functions.search('all', '', '')

    def showStats():
        functions.stats()

    def editStatus():
        functions.editAsList(dbConnection.showAll())

    window = tk.Tk()

    window.title("Invitee Register")
    window.geometry('1080x720')

    header = tk.Label(window, text="INVITATION REGISTER", font=('courier', 20, 'bold'))
    header.pack(ipady=5)

    credit = tk.Label(window, text="                              - Soumava Seal", font=('courier', 20, 'italic'))
    credit.pack()

    a = dbConnection.showAll()
    show(a)

    addbutton = tk.Button(window, text="Add", command=add, width=10, height=2)
    addbutton.place(x=50, y=625)

    updateButton = tk.Button(window, text="Update", command=updatedView, width=10, height=2)
    updateButton.place(x=280, y=625)

    statButton = tk.Button(window, text="Show Stats", command=showStats, width=10, height=2)
    statButton.place(x=510, y=625)

    editButton = tk.Button(window, text='Edit Status', command=editStatus, width=10, height=2)
    editButton.place(x=740, y= 625)

    searchButton = tk.Button(window, text="Search", command=search, width=10, height=2)
    searchButton.place(x=950, y=625)

    window.mainloop()


homeWindow()
