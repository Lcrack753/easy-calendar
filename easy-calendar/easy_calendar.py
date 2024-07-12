from enum import Enum, auto
from datetime import datetime
from collections import Counter
from pprint import pprint
from dataclasses import dataclass, field
from calendar import Calendar
# Constantes para los meses
class Months(Enum):
    ENERO = 1
    FEBRERO = 2
    MARZO = 3
    ABRIL = 4
    MAYO = 5
    JUNIO = 6
    JULIO = 7
    AGOSTO = 8
    SEPTIEMBRE = 9
    OCTUBRE = 10
    NOVIEMBRE = 11
    DICIEMBRE = 12

# Constantes para los días
class Days(Enum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4
    SABADO = 5
    DOMINGO = 6

# Número de días por mes
mdays = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]





@dataclass
class Day:
    date: datetime
    data: list = field(default_factory=list)
    
    def __post_init__(self):
        self.meta_data = Days(self.date.weekday())
@dataclass
class Month:
    meta_data: Months
    days: list[Day] = field(default_factory=list)

@dataclass
class Year:
    year: int
    months: list[Month] = field(default_factory=list)



class EasyCalendar():
    def __init__(self, dates=None, format=r'%Y-%m-%d'):
        self.dates = dates
        self.format = format

    def count_dates(self, dates):
        count = Counter()
        count_month = Counter()
        count_week = Counter()
        if dates is None:
            return 0
        
        for d in dates:
            if isinstance(d, dict):
                d = d['date']
            try:
                d = datetime.strptime(d, self.format)
            except ValueError:
                raise ValueError(f"Fechas deben ser válidas, formato actual: {self.format}")
            count[d.strftime(r'%Y-%m-%d')] += 1
            count_month[d.strftime(r'%m-%d')] += 1
            count_week[Days(d.weekday()).name] += 1
        return count, count_month, count_week

    # def generic(self, stamp: chr = 'y'):
    #     assert stamp in ['y','m','w']
    #     cal = []
    #     match stamp:
    #         case 'w':
    #             for day in Dia:
    #                 cal.append({
                        
    #                 })     

    def year_formated(self, year: int = 2024):
        cal = Year(year)
        for month in Months:
            py_cal = [day for week in Calendar().monthdatescalendar(year, month.value) for day in week]
            month_obj = Month(meta_data=Month, days=[Day(day) for day in py_cal])
            for day in py_cal:
                month_obj.days.append(Day(day))
            cal.months.append(Month)
      



def main():
    dates = ['2024-08-15', '2024-08-15', '2024-08-10', '2024-08-08', '2024-08-10']
    dates = [{'date':'2024-05-06', 'id': 155, 'url': 'https://'},
             {'date':'2024-05-06', 'id': 155, 'url': 'https://'},
             {'date':'2022-05-01', 'id': 155, 'url': 'https://'},
             {'date':'2024-05-01', 'id': 155, 'url': 'https://'},
             {'date':'2026-07-06', 'id': 155, 'url': 'https://'}]
    cal = EasyCalendar(dates=dates)
    # pprint(cal.count_dates())
    print(Calendar().yeardatescalendar(2024))

if __name__ == '__main__':
    main()