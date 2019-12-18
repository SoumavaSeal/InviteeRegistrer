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
        functions.search()

    window = tk.Tk()

    window.title("Invitee Register")
    window.geometry('1080x720')

    header = tk.Label(window, text="INVITATION REGISTER", font=42)
    header.pack(ipady=5)

    credit = tk.Label(window, text="                                    - Soumava Seal", font='10')
    credit.pack()

    a = dbConnection.showAll()
    show(a)

    addbutton = tk.Button(window, text="Add", command=add, width=10, height=2)
    addbutton.place(x=100, y=625)

    updateButton = tk.Button(window, text="Update", command=updatedView, width=10, height=2)
    updateButton.place(x=500, y=625)

    editButton = tk.Button(window, text="Search", command=search, width=10, height=2)
    editButton.place(x=900, y=625)

    window.mainloop()


homeWindow()
