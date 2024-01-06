#append= listenin sonuna eleman ekle
#insert= listenin istenilen yerine eleman ekler
#remove= listeden eleman çıkarır
#extend= listeye birden fazla eleman ekler
#pop= listenin en son elemanını siler ve döndürür
#reverse= listeyi tersine döndüren metod
#sort ve sorted= sort listeyi sıralar 
    #/ sorted hem sıralıyor hemde bozmuyor listeyi
#min, max ve in= min bir listedeki en küçük elemanı döndürür 
    #/ max listenin en büyük elemanını döndürür 
        #/ in listenin içinde verilen eleman olup olmadığını sorgular
#sum= elemanları toplar
#enumerate= numaralandırır elemanları
#join= elemanları string e çevirir
#split= string elemanları parçalayıp listeye atar


#   renkler = ["Siyah","Beyaz","Sarı","Mavi","Yeşil"]
#   print(renkler[1::2])


renkler = ["Siyah","Beyaz","Sarı","Mavi","Yeşil"]

#print(renkler)
#renkler.append("Gri")
#print(renkler)


#renkler.insert(0,"Gri")
#print(renkler)

#renkler.remove("Sarı")
#print(renkler)

#renkler2 = ("Turuncu","Mavi","Mor","Kahverengi")
#renkler.extend(renkler2)
#print(renkler)

#silinen = renkler.pop()
#print(renkler)
#print(silinen)

#print(renkler)
#renkler.reverse()
#print(renkler)

#print(renkler)
#renkler.sort()
#print(renkler)

#print(renkler)
#renkler.sort(reverse=True)
#print(renkler)

#print(renkler)
#liste2= sorted(renkler)
#print(liste2)
#print(renkler)

sayilar = [2,3,12,54,23,56,43,1,7]

#print(min(sayilar))
#print(max(sayilar))

#print(sum(sayilar))

#for renk in renkler:
#    print(renk)


#print(list(enumerate(renkler,start=3)))

#print("Bordu" in renkler)


stringrenkler = "-".join(renkler)
print(stringrenkler)

renkler2 = stringrenkler.split("-")
print(renkler2)

