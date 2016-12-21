import datetime
today = datetime.datetime.today()
print('Today is:', today)

for attr in \
    ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr, getattr(today, attr))
print('Time:', today.hour, ':', today.minute)