import datetime

dt_kst = datetime.datetime.utcnow()+datetime.timedelta(hours=9)
print(dt_kst.strftime("%Y-%m-%d"))
