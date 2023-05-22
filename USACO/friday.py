"""
ID: joshua.31
PROG: friday
LANG: PYTHON3
"""

years = int(open('friday.in', 'r').read())
dates = [0, 0, 0, 0, 0, 0, 0]  # sat, sun, mon ... fri


def get_feb(y):
    if y % 4 == 0:
        if y % 400 == 0:
            return 29
        elif y % 100 == 0:
            return 28
        else:
            return 29
    else:
        return 28


def get_thirteenth(first_day):
    return (first_day + 5) % 7


def get_next_month_first_day(first_day, total_days):
    return (first_day + total_days) % 7


day = 2  # 0 - sat, 1 - sun, 6 - fri
for year in range(1900, 1900 + years):
    months = [31, get_feb(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in months:
        dates[get_thirteenth(day)] += 1
        day = get_next_month_first_day(day, month)

out = open('friday.out', 'w')
out.write(' '.join([str(x) for x in dates]))
out.write('\n')
out.close()