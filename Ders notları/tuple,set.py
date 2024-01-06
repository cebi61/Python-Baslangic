#Tuple(Demet)= Eleman eklenmez,silinmez ve değiştirilmez.
#Set(küme)= (sırası bir yapısı vardır)



#Demet = ("Sarı","Mavi","Yeşil","Kırmızı","Siyah")

kume = {"Sarı","Mavi","Yeşil","Kırmızı","Siyah"}

#print(kume)

#kume.add("Pembe")
#eleman ekler

#kume.remove("Sarı")
#kümeden eleman çıkarır

#kume.discard("Gri")
#çıkarırken içinde olmasa bile hata vermez.

kume1 = {"Sarı","Mavi","Yeşil","Kırmızı","Siyah"}
kume2 = {"Sarı","Mavi","Yeşil","Beyaz","Gri"}



#print(kume1.intersection(kume2))
#kümeleri kesiştirir (intersection)

#print(kume1.union(kume2))
#kümeleri birleştirir ve fazla olanları bir kere yazar.(union)

#print(kume1.difference(kume2))
#Kümeler arasındaki farkı yazar.(difference)

#print("Beyaz" in kume1.union(kume2))
#'in' kümelerin içinde eleman arar

bosliste1 = []  #boş küme
bosliste2 = list()  #boş küme

bosdemet1 = ()  #boş küme
bosdemet2 = tuple() #boş küme

boskume1 = set() #boş küme
boskume2 = {} # bu bir sözlüktür boş küme oluşturmaz

python = set("PYTHON")
print (python)