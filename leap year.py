def is_leap_year(year):
   
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def find_anniversary(date):
    day, month, year = map(int, date.split('/'))

    if is_leap_year(year):
        print(f"Given Anniversary Year: Leap Year. Anniversary Date: {day:02d}/{month:02d}/{year - 1}")
    else:
        print(f"Given Anniversary Year: Non Leap Year. Anniversary Date: {day:02d}/{month:02d}/{year - 1}")

date = "04/11/2024"

find_anniversary(date)
