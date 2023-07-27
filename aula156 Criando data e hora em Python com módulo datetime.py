# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

# from pytz import timezone
# data = datetime.now(timezone('America/Santiago'))


data = datetime.now()
datas = data.timestamp()
datass = datetime.fromtimestamp(datas)
print(data.timestamp())
print(datetime.fromtimestamp(1683678912.846215))
print(datass)


# data_str_data = '2023-5-9 07:56:20'
# data_str_fort = '%Y-%m-%d %H:%M:%S'
# data_str_data2 = '2023/5/9 07:56:20'
# data_str_fort2 = '%Y/%m/%d %H:%M:%S'

# data = datetime(2023, 5, 9, 7, 56, 20, tzinfo=timezone('America/Santiago'))

# print(data)
# data =  datetime.strptime(data_str_data2, data_str_fort2 )
