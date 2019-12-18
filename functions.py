import tkinter as tk
import tkinter.ttk as ttk
import dbConnection


def add(): # def daysCount():
    #     days = 0
    #     if chkState_1.get() == 1:
    #         days = days + 1
    #
    #     if chkState_2.get() == 1:
    #         days = days + 1
    #
    #     if chkState_3.get() == 1:
    #         days = days + 1
    #
    #     return days

    def addEntry():

        a = dbConnection.showAll()
        if len(a) == 0:
            serial = 1

        else:
            serial = int(a[len(a) - 1][4]) + 1

        values = [nameInput.get(), memberNoInput.get(), daysInput.get(), relationInput.get(), str(serial), statusCombo.get()]
        dbConnection.addNewEntry(values)
        addwindow.destroy()

    addwindow = tk.Tk()

    addwindow.title("Add a new Entry")
    addwindow.geometry('480x300')

    header = tk.Label(addwindow, text="Add a new Entry", font=30)
    header.place(x=180, y=5)

    name = tk.Label(addwindow, text="Name of the family representetive :- ")
    name.place(x=5, y=50)
    nameInput = tk.Entry(addwindow)
    nameInput.place(x=210, y=50, width=200)

    memberNo = tk.Label(addwindow, text="No. of the family members :- ")
    memberNo.place(y=80, x=5)
    memberNoInput = tk.Entry(addwindow)
    memberNoInput.place(x=180, y=80, width=50)

    days = tk.Label(addwindow, text="No of days Invited For :-")
    days.place(x=5, y=110)
    daysInput = tk.Entry(addwindow)
    daysInput.place(x=150, y=110, width=50)

    relation = tk.Label(addwindow, text="Relation :-")
    relation.place(x=5, y=140)
    relationInput = tk.Entry(addwindow)
    relationInput.place(x=80, y=140, width=200)

    status = tk.Label(addwindow, text="Invitation Status :- ")
    status.place(x=5, y=170)

    statusCombo = ttk.Combobox(addwindow)
    statusCombo['values'] = ('Pending', 'Invited', "Invited but won't come")
    statusCombo.place(x=150, y=170)
    statusCombo.current(0)

    button = tk.Button(addwindow, text="Add", font=20, command=addEntry)
    button.place(x=230, y=220)

    nameInput.focus()
    addwindow.after(1, lambda: addwindow.focus_force())

    addwindow.mainloop()


def show(window, a):
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), height=493, width=1080)

    myframe = tk.Frame(window, bd=1)
    myframe.pack(fill=tk.X, ipady=20)

    canvas = tk.Canvas(myframe)

    mylist = tk.Frame(canvas, width=1080)

    myscrollbar = tk.Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.X)
    canvas.create_window((0, 0), window=mylist, anchor='nw')
    mylist.config(width=1080)
    mylist.bind("<Configure>", myfunction)

    head_1 = tk.Label(mylist, width=35, text="Name", borderwidth=1, relief="solid", bg="orange")
    head_2 = tk.Label(mylist, width=30, text="Number of Family Members", borderwidth=1, relief="solid", bg="orange")
    head_3 = tk.Label(mylist, width=20, text="Days invited", borderwidth=1, relief="solid", bg="orange")
    head_4 = tk.Label(mylist, width=30, text="Relation", borderwidth=1, relief="solid", bg="orange")
    head_5 = tk.Label(mylist, width=15, text="Registration No.", borderwidth=1, relief="solid", bg="orange")
    head_6 = tk.Label(mylist, width=25, text="Status", borderwidth=1, relief="solid", bg="orange")

    head_1.grid(column=1, row=0)
    head_2.grid(column=2, row=0)
    head_3.grid(column=3, row=0)
    head_4.grid(column=4, row=0)
    head_5.grid(column=0, row=0)
    head_6.grid(column=5, row=0)

    # col_1 = tk.Label(mylist,text="soumava")

    for i in range(len(a)):
        col_1 = tk.Label(mylist, width=35, text=a[i][0], borderwidth=1, relief="solid")
        col_2 = tk.Label(mylist, width=30, text=str(a[i][1]), borderwidth=1, relief="solid")
        col_3 = tk.Label(mylist, width=20, text=str(a[i][2]), borderwidth=1, relief="solid")
        col_4 = tk.Label(mylist, width=30, text=str(a[i][3]), borderwidth=1, relief="solid")
        col_5 = tk.Label(mylist, width=15, text=str(a[i][4]), borderwidth=1, relief="solid")
        col_6 = tk.Label(mylist, width=25, text=str(a[i][5]), borderwidth=1, relief="solid")

        col_1.grid(column=1, row=1 + i)
        col_2.grid(column=2, row=1 + i)
        col_3.grid(column=3, row=1 + i)
        col_4.grid(column=4, row=1 + i)
        col_5.grid(column=0, row=1 + i)
        col_6.grid(column=5, row=1 + i)

        # mylist.insert(tk.END, col_1.cget('text'))

    # mylist.pack(fill=tk.X)
    # scrollbar.config(command=mylist.yview)


def search():
    def searchResults():
        name = promtInput.get()
        a = dbConnection.searchByName(name)
        searchWindow.destroy()

        def editInitialize():
            if len(a) == 1:
                tempWindow.destroy()
                edit(a)

            else:
                def startedit():
                    i = int(promtInput1.get())
                    p = dbConnection.searchByRegistrationNo(i)
                    tempWindow2.destroy()
                    tempWindow.destroy()
                    edit(p)

                tempWindow2 = tk.Tk()
                prompt1 = tk.Label(tempWindow2,
                                   text="Multiple Results Detected!! Enter the Registration Number of the entry you want to edit",
                                   font=2)
                prompt1.pack(pady=5)
                promtInput1 = tk.Entry(tempWindow2)
                promtInput1.pack(pady=5)
                promtInput1.focus()
                tempWindow2.after(1, lambda: tempWindow2.focus_force())
                enterButton = tk.Button(tempWindow2, width=10, height=2, text="Enter", command=startedit)
                enterButton.pack()

                tempWindow2.mainloop()

        tempWindow = tk.Tk()

        header = tk.Label(tempWindow, text="Search Results", font=2)
        header.pack()
        show(tempWindow, a)
        editButton = tk.Button(tempWindow, text='Edit', width=10, height=2, command=editInitialize)
        editButton.pack()

        tempWindow.mainloop()

    searchWindow = tk.Tk()

    searchWindow.geometry("480x180")

    prompt = tk.Label(searchWindow, text="Enter the name of the family representetive :- ", padx=10, pady=20)
    prompt.grid(row=1, column=0)

    promtInput = tk.Entry(searchWindow)
    promtInput.grid(row=1, column=1)

    promtInput.focus()
    searchWindow.after(1, lambda: searchWindow.focus_force())

    searchButton = tk.Button(searchWindow, width=10, text="Search", command=searchResults)
    searchButton.place(x=200, y=80)

    searchWindow.mainloop()


def edit(a):

    def deleteEntry():
        dbConnection.deleteByRegistrationNo(a[0][4])
        editWindow.destroy()

    def editEntry():
        values = [nameInput.get(), memberNoInput.get(), daysInput.get(), relationInput.get(), a[0][4], statusCombo.get()]
        dbConnection.updateEntry(values)
        editWindow.destroy()


    editWindow = tk.Tk()

    editWindow.title("Edit an existing Entry")
    editWindow.geometry('480x300')

    header = tk.Label(editWindow, text="Edit an existing Entry", font=30)
    header.place(x=150, y=5)

    name = tk.Label(editWindow, text="Name of the family representetive :- ")
    name.place(x=5, y=50)
    nameInput = tk.Entry(editWindow)
    nameInput.place(x=210, y=50, width=200)
    nameInput.insert(0, a[0][0])

    memberNo = tk.Label(editWindow, text="No. of the family members :- ")
    memberNo.place(y=80, x=5)
    memberNoInput = tk.Entry(editWindow)
    memberNoInput.place(x=180, y=80, width=50)
    memberNoInput.insert(0, a[0][1])

    days = tk.Label(editWindow, text="No of days Invited For :-")
    days.place(x=5, y=110)
    daysInput = tk.Entry(editWindow)
    daysInput.place(x=150, y=110, width=50)
    daysInput.insert(0, a[0][2])

    relation = tk.Label(editWindow, text="Relation :-")
    relation.place(x=5, y=140)
    relationInput = tk.Entry(editWindow)
    relationInput.place(x=80, y=140, width=200)
    relationInput.insert(0, a[0][3])

    status = tk.Label(editWindow, text="Invitation Status :- ")
    status.place(x=5, y=170)


    statusCombo = ttk.Combobox(editWindow)
    options = ['Pending', 'Invited', "Invited but won't come"]
    statusCombo['values'] = options
    statusCombo.place(x=150, y=170)
    index = 0
    while options[index] != a[0][5]:
        index = index + 1

    statusCombo.current(index)

    button = tk.Button(editWindow, text="Save", font=20, command=editEntry)
    button.place(x=150, y=220)

    deleteButton = tk.Button(editWindow, text="Delete", font=20, command=deleteEntry)
    deleteButton.place(x=280, y=220)

    nameInput.focus()
    editWindow.after(1, lambda: editWindow.focus_force())

    editWindow.mainloop()


def stats():
    def showList(i, days, status):
        tempWindow = tk.Tk()
        if i==1:
            p = dbConnection.dayInvitation(days)
        elif i==2:
            p =dbConnection.invitationStatus(status)
        headerText = "Guests registered for " + days + "-day invitation"
        header = tk.Label(tempWindow, text=headerText, font=('times', 20, 'bold'))
        header.pack()
        show(tempWindow, p)
        searchbtn =tk.Button(tempWindow, text="search", width=10, height=2, command=search)
        searchbtn.pack()
        tempWindow.mainloop()

    def onedayList():
        showList(1, '1', '')

    def twodayList():
        showList(1, '2', '')

    def threedayList():
        showList(1, '3', '')

    def statusInvited():
        showList(2, '', 'Invited')

    def statusPending():
        showList(2, '', 'Pending')

    def noOfGuests(a):
        guests = 0
        for item in a:
            guests = guests + int(item[1])

        return guests

    statWindow = tk.Tk()
    statWindow.title("Statistics")
    statWindow.geometry("480x300")

    header = tk.Label(statWindow, text="Take a look on your Stats!!", font=('times', 20, 'bold'))
    header.pack(ipady=5)

    label_1 = tk.Label(statWindow)
    label_1_Result = "Total no of Guests Registered = " + str(noOfGuests(dbConnection.showAll()))
    label_1.config(text=label_1_Result, font=("", 12, 'italic'))
    label_1.place(x=50, y=60)

    label_2 = tk.Label(statWindow)
    label_2_Result = "No of Guests registered for 1-day invitation = " + str(noOfGuests(dbConnection.dayInvitation('1')))
    label_2.config(text=label_2_Result, font=("", 10, ''))
    label_2.place(x=80, y=100)
    onedayButton = tk.Button(statWindow, text="view List", width=10, height=1, command=onedayList)
    onedayButton.place(x=380, y=95)

    label_3 = tk.Label(statWindow)
    label_3_Result = "No of Guests registered for 2-day invitation = " + str(noOfGuests(dbConnection.dayInvitation('2')))
    label_3.config(text=label_3_Result, font=("", 10, ''))
    label_3.place(x=80, y=135)
    twodayButton = tk.Button(statWindow, text="view List", width=10, height=1, command=twodayList)
    twodayButton.place(x=380, y=130)

    label_4 = tk.Label(statWindow)
    label_4_Result = "No of Guests registered for 3-day invitation = " + str(noOfGuests(dbConnection.dayInvitation('2')))
    label_4.config(text=label_4_Result, font=("", 10, ''))
    label_4.place(x=80, y=170)
    threedayButton = tk.Button(statWindow, text="view List", width=10, height=1, command=threedayList)
    threedayButton.place(x=380, y=165)

    label_5 = tk.Label(statWindow)
    label_5_text = "Total number of guests invited = " + str(noOfGuests(dbConnection.invitationStatus('Invited')))
    label_5.config(text=label_5_text, font=('times', 15, 'italic'))
    label_5.place(x=50, y=230)
    label_5_Btn = tk.Button(statWindow, text="View List", width=10, command=statusInvited)
    label_5_Btn.place(x=380, y=225)

    label_6 = tk.Label(statWindow)
    label_6_text = "No of invitation Pending = " + str(noOfGuests(dbConnection.invitationStatus('Pending')))
    label_6.config(text=label_6_text, font=('times', 15, 'italic'))
    label_6.place(x=50, y=260)
    label_6_Btn = tk.Button(statWindow, text="View List", width=10, command=statusPending)
    label_6_Btn.place(x=380, y=255)

    statWindow.mainloop()

# stats()
