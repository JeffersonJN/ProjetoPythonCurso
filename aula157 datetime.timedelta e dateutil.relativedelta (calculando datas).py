# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('23/11/1994 17:30:30', fmt)
data_fim = datetime.strptime('09/05/2023 21:59:20', fmt)
data_now = datetime.now()  

# delta = timedelta(weeks=52, days=365, hours=20,)
# print(data_now + delta)
delta = relativedelta(data_now, data_inicio)

# print(data_now + relativedelta(seconds=59, minutes=20, days=20, weeks=5, months=2, years=3))
print(delta.years, delta.months, delta.days, delta.hours, delta.minutes, delta.seconds, delta.microseconds )



# delta = data_fim - data_inicio
# print(delta.days, delta.seconds)
# print(delta.total_seconds())
# print(delta)

# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)