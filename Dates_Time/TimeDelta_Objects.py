from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    # construct a basic timedelta and print it
    print(timedelta(days=365, hours=5, minutes=1))

    # print today's date
    now = datetime.now()
    print("Today is: ", now)

    # print today's date one year from now
    print("One year from now it will be: " + str(now + timedelta(days=365)))

    # create a timedelta that use more than one argument
    print("In 2 days and 3 weeks, it will be: " + str(now + timedelta(days=2, weeks=3)))

    # calculate the date 1 week ago, formatted as a string
    t = now - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was: " + s)

    # How many days until April Fool's Day?
    today = date.today()
    afd = date(today.year, 4, 1)

    # Use date comparison to see if April Fool's Day has already gone for this year
    # If it has, use the replace() function to get the date for next year
    if afd < today:
        print("April Fool's Day already went by %d days ago" % (today - afd).days)
        afd = afd.replace(year=today.year + 1)

    # Calculate the amount of time until April Fool's Day
    time_to_afd = afd - today
    print("It's just ", time_to_afd.days, "days until April Fool's Day")


if __name__ == '__main__':
    main()
