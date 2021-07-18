import random
for i in range(10):
    x = int(input("Bir sayı gir: "))
    y = int(input("Daha büyük bir sayı gir : "))
    the_number = random.randint(x, y)
    guess = int(input( str(x) +" ve " + str(y)+ " arasında bir sayı tahmin et: "))
    while guess != the_number:
        if guess > the_number:
            print(guess, "çok yüksekti. Tekrar deneyin")
        if guess < the_number:
            print(guess, "çok düşüktü. Tekrar deneyin.")
        guess = int(input("Tekrar tahmin et: "))
    print(guess, "numaraydı! Sen kazandın!")
