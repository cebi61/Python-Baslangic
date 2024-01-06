# 10000 e kadar olan asal sayıları ve bu asal sayıların 3 ve 7 ile başlayıp bitenlerini yazıyor
# prime_list = list ()

# prime_list.append(2)

# sayi = 3

# while True:
#     prime = True
#     for i in range(2,int(sayi** 0.5)+1):
#         if sayi %i == 0:
#             prime = False
#             break
#     if prime:
#         prime_list.append(sayi)
#         if len (prime_list) ==10000:
#             break
#     sayi += 1

# liste2 = []

# for prime in prime_list:
#     strprime = str(prime)
#     if strprime.startswith("3") and strprime.endswith ("7"):
#         liste2.append(prime)
# print(liste2)
# print(len(liste2))


#_________________________________________________________________________

# liste = []
# for sayi in range (100,1000):
#     toplam = 0
#     gecici_sayi = sayi
#     while gecici_sayi != 0:
#         basamak = gecici_sayi %10
#         toplam += basamak ** 3
#         gecici_sayi //= 10
#     if toplam == sayi:
#         liste.append(sayi)
# print(liste)

#____________________________________________________________________________________________________

# fibonacci_list = []
# fibonacci_list.append(1)
# fibonacci_list.append(1)

# index = 2
# while True:
#     fibonacci_list.append(fibonacci_list[index - 2]+fibonacci_list[index - 1])
#     index += 1
#     if len(fibonacci_list) == 100:
#         break
# print(fibonacci_list)

#______________________________________________________________________________________________________

# fibonacci_list = list()
# fibonacci_list.append(1)
# fibonacci_list.append(2)

# index = 2
# while True:
#     fibonacci_list.append(fibonacci_list[index - 2]+fibonacci_list[index - 1])
#     terim = fibonacci_list[index - 2] + fibonacci_list[index - 1]
#     if len(str(terim)) == 1000:
#         print(terim)
#         break
#     index += 1


