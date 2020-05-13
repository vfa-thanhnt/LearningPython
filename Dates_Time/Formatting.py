from datetime import datetime


def main():
    # Time and dates can be formatted using a set of predefined string
    now = datetime.now()

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y"))

    print(now.strftime("%a, %d %B, %y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale's date and time: %c"))
    print(now.strftime("Locale's date: %x"))
    print(now.strftime("Locale's time: %X"))

    # %I/%H - 12/24 Hour, %M - minute, %C - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))


if __name__ == '__main__':
    main()
