
# sayi = input("Bir Sayı Giriniz:")
# print(sayi)

# sayi = int(input("Bir Sayı Giriniz:"))
# faktoriyel = 1
# for i in range (1,sayi+1):
#     faktoriyel *= i
# print (f"{sayi}! = {faktoriyel}")



# sayi = int(input("Bir Sayı Giriniz:"))
# prime = True
# for i in range(2,sayi):
#     if sayi %i == 0:
#         prime = False
#         break
# if prime == True:
#     print(f"{sayi} Sayısı asaldır")
# else:
#     print(f"{sayi} Sayısı asal değildir")   



# sayi = int(input("Bir Sayı Giriniz:"))
# bolen_sayisi = 0
# for i in range(1,sayi+1):
#  if sayi %i == 0:
#   bolen_sayisi += 1
# print(f"{sayi} Sayısının {bolen_sayisi} tane böleni vardır.")


#
# sayi = int(input("Bir Sayı Giriniz:"))
# str_sayi= str(sayi)
# toplam = 0
# for rakam in str_sayi:
#     toplam += int(rakam)
# print(toplam)


#5 sayı istiyor istenilen listedeki en küçük ve en büyük sayıları yazıyor
# liste = []
# for i in range(5):
#     sayi = int(input("Bir Sayı Giriniz:"))
#     liste.append(sayi)
# print(f"En büyük sayı:{max(liste)}")
# print(f"En küçük sayı:{min(liste)}")


#Sayının Tamkare olup olmadığını hesaplıyor
# sayi = int(input("Bir Sayı Giriniz:"))
# karekok = sayi ** 0.5
# if karekok == int(karekok):
#     print("Karekök")
# else:
#     print("Tamkare değil")


#sözlükte kaç karakter var onu buluyor
# metin =(input("Bir Metin Giriniz:"))
# sozluk = dict()
# for harf in metin:
#     if harf in sozluk:
#         sozluk[harf] += 1
#     else:
#         sozluk[harf] = 1
# for harf,adet in sozluk.items():
#     print(harf,adet)


#ekranda okunan bir metinde a harflerini büyük yapan bir program
# metin = input("Bir metin giriniz:")
# metin2= ""

# for harf in metin:
#     if harf == "a":
#         metin2 += "A"
#     else:
#         metin2 += harf
# print(metin2)