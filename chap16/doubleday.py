import time
from datetime import *

def week_day():
    todays_date=date.today()
    todays_weekday= datetime.weekday(todays_date)
    weekdays={6:'Sunday',0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday'}
    return weekdays[todays_weekday]



def birthday_countdown(birthday):
    """Takes tuple containing day followed by month (int representation) as a birthday. Returns time to next birthday."""
    today = datetime.today()
    next_birthday = datetime(today.year, birthday[1], birthday[0])
    if next_birthday <= today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    time_to_birthday = abs(next_birthday - today)
    return time_to_birthday
    


def age(birthdate):
    """Takes a tuple containing day followed by month (int representation) followed by year as a birthdate. Returns age of person with said birthdate in days."""
    today=date.today()
    birthdate=date(birthdate[2],birthdate[1],birthdate[0])
    if birthdate>today:
        return "Person has not been born yet!"
    difference=today-birthdate
    return difference.days

def doubleday(birthdate1,birthdate2):
    """Takes two tuples of the form (day,month,year). Returns the day that the elder is twice as old as the younger."""
    b1=date(birthdate1[2],birthdate1[1],birthdate1[0])
    b2=date(birthdate2[2],birthdate2[1],birthdate2[0])
    diff= abs(b1-b2)
    doubleday=max(b1,b2)+diff
    return doubleday


def nday(bdate1,bdate2, n):
    """Takes two tuples of the form (day,month,year), and an integer n. Returns the day that the elder is n as old as the younger."""
    b1=date(bdate1[2],bdate1[1],bdate1[0])
    b2=date(bdate2[2],bdate2[1],bdate2[0])
    diff= abs(b1-b2)
    nday=max(b1,b2)+diff*(n-1)
    return nday

if __name__ == "__main__":
    print week_day()
    print birthday_countdown((6,5))
    print age((6,5,1993))
    print doubleday((3,11,1972),(3,11,1998))
    print nday((28,1,1995),(6,5,1993),3)
