#if= doğru ise altındaki durumları gerçekleştirir değilse if bloğundan çıkar.
#and= çalışması için her koşul doğru olması lazım
#or= bir koşul bile doğru ise çalışır
#not= içinde bulunduğu koşulu olumsuza çevirir


# a= 5
# b= 5
# if a == b:
#     print("a eşittir b")
# else:
#     print("a ve b eşit değildir")



# renk = "Siyah"
# if renk == "Beyaz":
#     print("Beyaz")
# elif renk == "Sarı":
#     print("Sarı")
# elif renk == "Mavi":
#     print("Mavi")
# else:
#     print("Hiçbiri")



a = 5 
b = 8
c = 10

# if a > b or c == a:
#     print("koşul doğru")
# else:
#     print("koşul yanlış")

# if a < b and b < c:
#     print("koşul doğru")
# else:
#     print("koşul yanlış")


# liste = [1,2,3,4,5,6,7,8,9]
# a = 12
# if a in liste:
#     print("Listede var")
# else:
#     print("listede  yok")


# a = 8
# b = 10

# if not a == b:
#     print("koşul doğru")
# else:
#     print("Koşul yanlış")


a = "python"
b = "pytho"
b += "n"

if a ==b:
    print("a = b")
else:
    print("a != b")