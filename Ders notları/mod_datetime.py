from datetime import date
from datetime import datetime
from datetime import timedelta
# bugun = date.today()


#print(type(bugun))
# print(bugun)
# print(bugun.day)
# print(bugun.month)
# print(bugun.year)
# print(bugun.weekday())
# print(bugun.isoweekday())


# gecmis_tarih = date(1998,11,24)

# gecen_zaman = bugun - gecmis_tarih
# print(gecen_zaman)





# suan = datetime.now()
# bugun = date.today()
# print(suan)
# print(suan.day)
# print(suan.month)
# print(suan.year)
# print(suan.weekday())
# print(suan.isoweekday())
# print(suan.hour)
# print(suan.minute)
# print(suan.second)

# gecmis_an = datetime(2014,5,26,6,45,32,123)
# print(suan-gecmis_an)


# print(bugun.strftime("%d:%m:%Y"))
# print(suan.strftime("%d:%m:%Y"))

#_________________________________________________________________

pazar_sayisi = 0
for yil in range(1901,2001):
    for ay in range(1,13):
        if datetime(yil,ay,1).weekday() == 6:
            pazar_sayisi +=1

print(pazar_sayisi)




# suan = datetime.now()
# tdelta = timedelta(days=7,hours=5,seconds=69)
# print(suan + tdelta)
# print(suan-tdelta)