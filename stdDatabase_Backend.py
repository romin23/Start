import sqlite3
#backend


def studentData():
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, stdID text, Firstname text, Surname text,Parents text, DOB text, Age text,Branch text,Year text, Gender text, Mobile text,Bedno text ) ")
    con.commit()
    con.close()

def addStdRec(stdID,Firstname,Surname,Parents,DOB,Age, Branch, Year, Gender, Mobile, Bedno):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?)",( stdID,Firstname,Surname,Parents,DOB,Age, Branch, Year, Gender, Mobile, Bedno))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    con.close()
    return row

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("DELETE  FROM student WHERE id=?", (id,))
    con.commit()
    con.close

def searchData(stdID="", Firstname="" , Surname="" ,Parents="", DOB="" , Age="" ,Branch="",Year="", Gender="" , Mobile="", Bedno=""):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student WHERE stdID=? OR Firstname=? OR  Surname=? OR Parents=? OR DOB=? OR  Age=? OR Branch=? OR Year=? OR  Gender=? OR  Mobile=? OR Bedno=?", (stdID , Firstname , Surname , Parents, DOB , Age , Branch ,Year, Gender , Mobile, Bedno))
    row = cur.fetchall()
    con.close()
    return row

def dataUpdate( id ,stdID="", Firstname="" , Surname="" ,Parents="", DOB="" , Age="" ,Branch="",Year="", Gender="" , Mobile="", Bedno=""):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("UPDATE student SET stdID=? OR Firstname=?, Surname=?, Parents=?, DOB=?,  Age=?, Branch=?, Year=?,  Gender=?,  Mobile=?, Bedno=?, WHERE id=?", (stdID , Firstname , Surname ,Parents, DOB , Age ,Branch,Year, Gender , Mobile, Bedno, id ))
    con.commit()
    con.close()




studentData()



