import random

random_integer = random.randint(1, 50)
status=True

while status:
    angka=int(input("Masukkan angka: "))
    if angka==random_integer:
        print("Selamat, tebakanmu benar!")
        status=False
    elif angka > random_integer:
        print("Tebakanmu terlalu besar")
    else:
        print("Tebakanmu terlalu kecil")

