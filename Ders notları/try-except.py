try:
    a = 5
    b = 2
    c = a / b
    x = 3
    d = x
    isim = "Ali"
    karakter = isim[1]
    list_ = [1,2,3]
    m = list_[5]

except ZeroDivisionError as e:
    print(e)

except NameError as e:
    print(e)

except IndexError as e:
    print(e)

except Exception as e:
    print(e)


else:#hata olduğu zaman çalışmaz
    print("Else Bloğu Çalışıyor")
    print(c)
    print(karakter)

finally:#hata alsa bile çalışır
    print("finally bloğu çalışıyor.")