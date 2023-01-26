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
        


def runDatTing():
    con = sqlite3.connect("main.db")
    cur = con.cursor()

    def dbTableSetUp():
        cur.execute("CREATE TABLE bookings('datee', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M')")

    def dbInsertDateTuples ():
        for i in range(365):
            cur.execute("INSERT INTO bookings (datee) VALUES(?)", [dateFormatter(i)]) #needs to be in [] otherwise sqlite treats it as 4 spereate inputs split at the ' '
        con.commit()

  
    dbTableSetUp()
    dbInsertDateTuples()

runDatTing()