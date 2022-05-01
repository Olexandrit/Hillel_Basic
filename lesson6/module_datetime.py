import datetime as dt

print(dt.date(2021, 1, 1))
print(dt.date.today())

print(dt.time(12, 30, 10))

print(dt.datetime.now())
print(dt.datetime.now().time())
print(dt.datetime.now().date())

delta = dt.timedelta(days=7)
now = dt.datetime.now()

print(now - delta)  # date 7 days ago

date = dt.datetime(2022, 1, 1)
delta = now - date
print(delta.days, 'days since first of January')