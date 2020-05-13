
import calendar


def main():
    # create a plain text calendar
    c = calendar.TextCalendar(calendar.MONDAY)
    st = c.formatmonth(2017, 1, 0, 0)
    print(st)

    # create an HTML formatted calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    st = hc.formatmonth(2017, 1)
    print(st)

    # loop over the days of a month
    # zeroes mean that the day of the week is in an overlapping month
    c = calendar.TextCalendar(calendar.SUNDAY)
    for i in c.itermonthdays(2017, 8):
        print(i)

    for day in calendar.day_name:
        print(day)

    # Calculate days based on a rule: For example, consider
    # a team meeting on the first Friday of every month.
    # To figure out what days that would be for each month,
    # We can use this script:
    print("Team meetings will be on: ")
    for m in range(1, 13):
        # get month calendar
        cal = calendar.monthcalendar(2020, m)

        # get week 1 and week 2 of each month
        week_one = cal[0]
        week_two = cal[1]

        # check friday belongs to week 1 or week 2
        if week_one[calendar.FRIDAY] != 0:
            # get Friday date of week 1
            meet_day = week_one[calendar.FRIDAY]
        else:
            # get Friday date of week 2
            meet_day = week_two[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meet_day))


if __name__ == '__main__':
    main()
