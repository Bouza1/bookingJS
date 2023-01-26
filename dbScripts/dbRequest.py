import sqlite3

dateStr = 'Thu Jan 26 2023'



def dataPull(dateString):
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM bookings WHERE datee = ?", [dateString])
    data = cur.fetchone()
    return data

print(dataPull(dateStr))

timesToInput = ["Thu Jan 26 2023 10:00","Thu Jan 26 2023 9:00","Thu Jan 26 2023 7:00"]
alphaArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
numberArrays = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def formatDateNTimeStr(dateNtimeString):
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    username = 2449
    for time in timesToInput:
        dateNStringArray = time.split()
        fullTime = dateNStringArray[4]
        time = fullTime.split(':')
        i = numberArrays.index(int(time[0]))
        alphaTime = alphaArray[i]
        cur.execute(f'UPDATE bookings SET {alphaTime} = {username} WHERE datee = ?', ["Thu Jan 26 2023"])
        # cur.execute("INSERT INTO bookings ('7') VALUES (?) WHERE date = '" +dateStr+ "'", username)
        # cur.execute("INSERT INTO bookings '"+time+"' WHERE date = '"+ str(date) +"' VALUES '"+ str(username) +"'", str(time) )
    con.commit()
formatDateNTimeStr(timesToInput)

