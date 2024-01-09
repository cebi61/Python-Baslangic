# r= okuma modu
# w= yazma modu (içerisinde yazı varsa onu siler yazılan şeyi aktarır)
# r+= hem okuma hem yazma modu
# a= sonuna yazı ekleme modu
# b= binary cinsinden işlem yapma


# f = open("ders.txt","r")
# icerik = f.read()
# print(icerik)
# f.close()


# # with open("ders.txt","r") as f:
# #      icerik = f.readlines()
# #      print(icerik)
# #      for satir in icerik:
# #          print(satir,end="")


# # for i in range(10):
#     # print(i,end="-")

# with open("ders.txt") as f:
#     satir = f.readline()
#     print(satir,end="")
#     f.seek(0)
#     satir = f.readline()
#     print(satir,end="")

# with open("ders.txt") as f:
#     icerik = f.read(10)
#     print(icerik,end="")
#     icerik = f.read(10)
#     print(icerik,end="")
#     icerik = f.read(10)
#     print(icerik,end="")

# with open("ders.txt") as f:
#     okunacak_miktar = 10
#     icerik = f.read(okunacak_miktar)
#     while len(icerik) > 0:
#         print(icerik,end="")
#         icerik = f.read(okunacak_miktar)


# with open("ders.txt","w") as f:
#     f.write("Merhaba")


# with open("ders.txt","a") as f:
#     f.write("nas")



#dosya içeriğini kopyalama
# with open("ders.txt") as okunacak:
#     with open("ders2.txt","w") as yazilacak:
#         for satir in okunacak:
#             yazilacak.write(satir)


#binary cinsinden kopyalama
# with open("4247.jpg","rb") as okunacak:
#     with open("42472.jpg","wb") as yazilacak:
#         okunacak_miktar = 1024
#         icerik = okunacak.read(okunacak_miktar)
#         while len (icerik) > 0:
#             yazilacak.write(icerik)
#             icerik = okunacak.read(okunacak_miktar)
