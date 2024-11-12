from dateutil.relativedelta import relativedelta
from pprint import pprint
from datetime import date


def get_date_range(start_date, end_date):
    if start_date == end_date:
        return [start_date]

    return [
        start_date,
        *get_date_range(start_date + relativedelta(days = 1), end_date)
    ]


start_date = date(2024, 4, 1)
end_date = date(2024, 5, 1)
pprint(get_date_range(start_date, end_date))