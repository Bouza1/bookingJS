from datetime import date, timedelta
import sqlite3

unformattedDate = date.today()

def dateFormatter (number):
    newDate = unformattedDate + timedelta(days=number)
    day3Letter = newDate.strftime("%a")
    day = newDate.strftime("%d")
    month = newDate.strftime("%b")
    year = newDate.strftime("%Y")
    return day3Letter + ' ' + month + ' ' + day  + ' ' + year
        

def dbTableSetUp():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE bookings(date, '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19')")


def dbInsertDateTuples ():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    for i in range(365):
        cur.execute("INSERT INTO bookings (date) VALUES(?)", [dateFormatter(i)]) #needs to be in [] otherwise sqlite treats it as 4 spereate inputs split at the ' '
    con.commit()

def runDatTing():
    dbTableSetUp()
    dbInsertDateTuples()
