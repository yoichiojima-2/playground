from dateutil.relativedelta import relativedelta
from pprint import pprint
from datetime import date


start_date = date(2024, 4, 1)
end_date = date(2024, 5, 1)

def get_date_range(d):
    if d == start_date:
        return d
    return get_date_range(d - relativedelta(days = 1))


pprint(get_date_range(end_date))