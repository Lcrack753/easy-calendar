from dataclasses import dataclass
from calendar import Calendar
from enum import Enum, global_enum
from pprint import pprint


@global_enum
class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

@global_enum
class Day(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


# Number of days per month (except for February in leap years)
mdays = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class EasyCalendar():
    def __init__(self, dates= []):


if __name__ == '__main__':
    main()