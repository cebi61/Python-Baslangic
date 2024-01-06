#Dictionaries (Sözlükler)=

kisi = {"isim":"ali","yas":20,"cinsiyet":"erkek","hobiler":["sinema","konser","yazılım"]}


#kisi["isim"] = "Ahmet"
#isimi güncelliyor

#kisi.update({"isim":"ahmet","yas":"35"})
#birden fazla alanı güncelliyor

#kisi["id"] = 12345
#alan eklemeye yarar

#del kisi["id"]
#alanı silmeye yarıyor

#for x in kisi:
#    print(kisi[x])
#for döngüsü ile bilgileri çekiyor

#print(kisi.keys())
#anahtar olan değerleri çeker

#print(kisi.values())
#değerleri çeker

#print(kisi.items())
#anahtarı ve değeri karşılıklı verir

#for k,v in kisi.items():
#    print(k,v)
#for döngüsünün ikili kullanımı


#print(kisi.get("id","Bulunamadı"))
#içinde bulunmasa bile get ile hata almazsın bulunuyorsa eleman gelir. ikinci anahtar ise if durumunda olması gereken durum(bulunamadı).
