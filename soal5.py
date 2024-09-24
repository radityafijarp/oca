tinggi=float(input("Masukan Tinggi: "))
berat=int(input("Masukan Berat: "))

imt = berat/(tinggi**2)
print(imt)
if imt<=18.5:
    print("Kurus")
elif imt <= 25:
    print("Normal")
elif imt <=30:
    print("Gemuk")
else:
    print("Kegemukan")

# #Float
# tinggi=1.65
# berat=67