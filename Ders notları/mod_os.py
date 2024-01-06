import os
from datetime import datetime

# print(os.getcwd())
# #dosyanın bulunduğu klasörü yazar

# os.chdir("C:\\Users\\adilc\\Desktop\\asd")
# print(os.getcwd())
#geçerli klasörü değiştirir


# print(os.listdir("C:\\Users\\adilc\\Desktop\\Oyunlar"))
# for dosya in os.listdir("C:\\Users\\adilc\\Desktop\\Oyunlar"):
#     print(dosya)
#klasörün içeriğini gösterir


# os.mkdir("DenemeKlasörü")
# klasör oluşturur


#os.makedirs("deneme1/deneme2/deneme3")
#iç içe birden fazla dosya oluşturma


# os.rmdir("DenemeKlasörü")
# belirtilen klasörü siler

#os.removedirs("deneme1/deneme2/deneme3")
# iç içe birden fazla dosya siliyor

# os.chdir('C:\\Users\\adilc\\Desktop\\asd')
# silinecek = os.listdir()[0]
# os.remove(silinecek)

#os.remove("Silinecek dosyanın konumu yazılır")

#mkdir, makedirs, rmdir, removedirs, remove




#Yeniden adlandırma aynı zamanda taşımak içinde kullanılabilir.
# os.chdir('C:\\Users\\adilc\\Desktop\\asd')
# os.rename('sd','değişen isim')

#dosya ile ilgili bilgiler veriyor
# os.chdir('C:\\Users\\adilc\\Desktop\\asd')
# print(os.stat('değişen isim').st_atime)
# zaman = datetime.fromtimestamp(os.stat('değişen isim').st_atime)

# print(zaman)


#birden fazla dosyayı gösterir(os.walk)
#os.chdir('C:\\Users\\adilc\\Desktop\\asd')
# for gecerli_klasör, icindeki_klasorler, icindeki_dosyalar in os.walk('C:\\Users\\adilc\\Desktop\\asd'):
#     print("Geçerli Klasör: ",gecerli_klasör)
#     print("İçindeki Klasörler: ",icindeki_klasorler)
#     print("İçindeki Dosyalar: ",icindeki_dosyalar)
#     print()



os.chdir('C:\\Users\\adilc\\Desktop\\asd')

#dosya yolu olucak şekilde dosyaları birleştiriyor
#print(os.path.join("Deneme1","Deneme2","Deneme3"))

# #dosya olup olmadığını sorguluyor true false döndürüyor
# print(os.path.isfile('C:\\Users\\adilc\\Desktop\\asd'))

# #klasör olup olmadığını sorguluyor true false döndürüyor
# print(os.path.isdir('C:\\Users\\adilc\\Desktop\\asd'))

#bir demet döndürür. doysa uzantısı ve türünü yazar
print(os.path.splitext('C:\\Users\\adilc\\Desktop\\asd'))