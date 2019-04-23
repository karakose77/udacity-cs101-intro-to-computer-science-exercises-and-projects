# Calculate days between two dates. Compensate for leap days.

daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    """
    Returns true if given year is a leap year.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def leap_days(y1, y2):
    """
    Returns the amount of total excess days for
    all the leap years between the years y1 and y2.
    """
    leap_days = 0
    y = y1
    while y < y2:
        leap_days += is_leap_year(y)
        y += 1
    return leap_days


def year_days(y1, y2):
    """
    Returns the total amount of days between y1 and y2
    leap days included.
    """
    return (y2 - y1) * 365 + leap_days(y1, y2)


def month_days(m1, m2):
    """
    Returns total amount of days between months m1 and m2.
    """
    m1_days = 0
    for m in range(m1-1):
        m1_days += daysInMonths[m]
    m2_days = 0
    for m in range(m2-1):
        m2_days += daysInMonths[m]
    return m2_days - m1_days


def day_days(d1, d2):
    """
    Returns total amount of days between days d1 and d2.
    """
    return d2 - d1


def days_between_dates(y1, m1, d1, y2, m2, d2):
    """
    Returns total amount of days between dates y1, m1, d1 and
    y2, m2, d2 leap days included.
    """
    result = year_days(y1, y2) + month_days(m1, m2) + day_days(d1, d2)
    if result >= 0:
        return result
    else:
        return "Current date can not be before the birth date!"


print(days_between_dates(1919, 4, 15, 2019, 4, 15))
