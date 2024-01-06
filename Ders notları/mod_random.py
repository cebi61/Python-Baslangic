#rasgele sayılar ve değerler üretiyor


import random

# for i in range(10):
#     print(random.random())
#0 ile 1 aralığında rasgele 10 sayı


# for i in range(10):
#      print(random.uniform(10,30))
# belirtilen sınıf aralığında rasgele 10 sayı


# for i in range(10):
#      print(random.randint(1,5))
# # tam sayı üretir. üst sınırı da dahil eder


# for i in range(10):
#      print(random.randrange(1,10,2))
# 3 fonksiyonundan rasgele sayı üretir. üst sınırı dahil ETMEZ.


liste = ["Siyah","Beyaz","Mavi","Yeşil","Gri","Turuncu"]

# print(random.choice(liste))
#print(liste)
#verilen listeden rasgele eleman seçer

# random.shuffle(liste)
# print(liste)
#listeyi karıştırır


# print(random.sample(liste,3))
#rasgele eleman seçiyor liste içinden


# zarlar = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
# for i in range(1000000):
#     zar = random.randint(1,6)
#     zarlar[zar] += 1
# for zar in zarlar:
#     print(f"{zar}gelme olasılığı:{zarlar[zar]/1000000}")
# zarların gelme olasılığını hesaplar


# alti_alti = 0
# deneme_sayisi = 0
# while True:
#     deneme_sayisi += 1
#     zar1 = random.randint(1,6)
#     zar2 = random.randint(1,6)
#     if zar1 == 6 and zar2 == 6:
#         alti_alti += 1
#     if alti_alti == 10:
#         print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atıldı.")
#         break
# 10 kere 6-6 gelme olasılığını hesaplar

