import random
for i in range(10):
    x = int(input("Bir sayı gir: "))
    y = int(input("Daha büyük bir sayı gir : "))
    sayi = random.randint(x, y)
    tahmin = int(input( str(x) +" ve " + str(y)+ " arasında bir sayı tahmin et: "))
    while tahmin != sayi:
        if tahmin > sayi:
            print(guess, "çok yüksekti. Tekrar deneyin")
        if tahmin < sayi:
            print(tahmin, "çok düşüktü. Tekrar deneyin.")
        tahmin = int(input("Tekrar tahmin et: "))
    print(tahmin, "numaraydı! Sen kazandın!")
