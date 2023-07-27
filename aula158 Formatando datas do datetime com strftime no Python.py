# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
data = datetime.strptime('2023-05-09 22:30:20', '%Y-%m-%d %H:%M:%S')
datas = datetime.now()
print(data)
print(data.strftime(fmt))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%d-%m-%Y %H:%M:%S'))

print(datas)
print(datas.strftime(fmt))
print(datas.strftime('%d/%m/%Y %H:%M:%S'))
print(datas.strftime('%d-%m-%Y %H:%M:%S'))
print(type('%Y'), datas.strftime('%Y'),type(datas.year), datas.year)
print(type('%m'), datas.strftime('%m'),type(datas.month), datas.month)
print(type('%d'), datas.strftime('%d'),type(datas.day), datas.day)

