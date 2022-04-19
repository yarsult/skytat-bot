import datetime


def sec(dayx, time):
    hour, mins = map(int, time.split(':'))
    today = datetime.datetime.now()
    date, month, year = map(int, today.strftime('%d %m %Y').split())
    if dayx == today.strftime('%w') and today > datetime.datetime(year, month, date, hour=hour,
                                                                  minute=mins):
        date += 1
    c = 0
    try:
        for day in range(date, date + 8):
            d = datetime.datetime(year, month, day, hour=hour, minute=mins)
            c += 1
            if d.strftime('%w') == dayx:
                return int((d - datetime.datetime.now()).total_seconds())
    except ValueError:
        for day in range(1, 8 - c):
            d = datetime.datetime(year, month + 1, day, hour=hour, minute=mins)
            if d.strftime('%w') == dayx:
                return int((d - datetime.datetime.now()).total_seconds())


