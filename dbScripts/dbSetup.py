from datetime import date, timedelta

unformattedDate = date.today()

def dateFormatter (number):
    newDate = unformattedDate + timedelta(days=number)
    day3Letter = newDate.strftime("%a")
    day = newDate.strftime("%d")
    month = newDate.strftime("%b")
    year = newDate.strftime("%Y")
    return day3Letter + ' ' + month + ' ' + day  + ' ' + year

def dbFirstSetUp ():
    for i in range (365):
        print(dateFormatter(i))

dbFirstSetUp()
