import sqlite3

conn = sqlite3.connect('wedding.db')


def conector():
    conn = sqlite3.connect('wedding.db')

    curs = conn.cursor()

    curs.execute('create table if not exists invitee (familyName, members ,daysInvited ,relation, registrationNo, status)')

    conn.commit()

    conn.close()


def addNewEntry(values):

    curs = conn.cursor()
    curs.execute("insert into invitee values(?,?,?,?,?,?)", values)
    conn.commit()


def showAll():
    cursor = conn.cursor()
    cursor.execute('select * from invitee')
    p = cursor.fetchall()
    conn.commit()
    return p


def searchByName(name):
    curs = conn.cursor()
    curs.execute("select * from invitee where familyName like '%" + name + "%'")
    p = curs.fetchall()
    conn.commit()
    return p


def searchByRegistrationNo(regNo):
    curs = conn.cursor()
    curs.execute("select * from invitee where registrationNo ='%s'" %regNo)
    p = curs.fetchall()
    conn.commit()
    return p


def deleteByRegistrationNo(regNo):
    curs = conn.cursor()
    curs.execute("delete from invitee where registrationNo = '%s'" %regNo)
    conn.commit()


def deleteAll():
    curs = conn.cursor()
    curs.execute("delete from invitee")
    conn.commit()


def addcolumn(name):
    curs = conn.cursor()
    curs.execute("alter table invitee add column "+name)
    conn.commit()


def updateEntry(values):
    curs = conn.cursor()
    query = "update invitee set familyName = '" + values[0] + \
        "', members = '" + values[1] + \
        "',daysInvited = '" + values[2] + \
        "', relation = '" + values[3] + \
        "', status = '" + values[5] + \
        "' where registrationNo = '" + values[4] + "'"
    curs.execute(query)
    conn.commit()
