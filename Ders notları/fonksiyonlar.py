# def bilgiler_ver():
#     print ("İşlem başarılı.")
#     print("Bloğun içerisi")
# bilgiler_ver()


# isim = input("İsminizi giriniz:")
# def selamla(isim):
#     print("Merhaba "+isim)
# selamla(isim)

# x = 4
# y = 9
# def topla(x,y):
#     print(f"x + y = {x+y}")
# topla(x,y)

# liste = [0,1,2,3,4,5,6,7,8,9,10]
# def ortalama_hesaplama(liste):
#     toplam = sum(liste)
#     adet = len(liste)
#     ortalama = toplam/adet
#     print(f"Girilen sayıların ortalaması: {ortalama}")
# ortalama_hesaplama(liste)


# def buyuk_harfe_cevir(metin):
#     metin = metin.upper()
#     print(metin)
# buyuk_harfe_cevir("asdasdsdakp")


# fiyat = int(input("Ürünün fiyatını giriniz!"))
# yuzde = int(input("Ürününe uygulanacak indirimi giriniz!"))
# def indirim_yap(fiyat,yuzde = 20):
#     indirim_miktarı = fiyat * (yuzde / 100)
#     indirimli_fiyat = fiyat - indirim_miktarı
#     print(f"İndirimli Tutar: {indirimli_fiyat}")

# indirim_yap(fiyat,yuzde)


def topla(x,y):
    print(x+y)
    return x + y #burda return kullanmazsak python o veriyi hafızada tutmaz ve başka yerde kullanamayız.
sonuc = topla(3,8)
print(sonuc)