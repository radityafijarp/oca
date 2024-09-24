bilangan=input("Masukan tiga bilangan: ")
list_bilangan=bilangan.split(" ")

total_sudut=float(list_bilangan[0])+float(list_bilangan[1])+float(list_bilangan[2])
# total_sudut=0
# for i in list_bilangan:
#     total_sudut=total_sudut+int(total_sudut[i])

if total_sudut==180:
    if list_bilangan[0]=="90" or list_bilangan [1]=="90" or list_bilangan[2]=="90":
        print("SEGITIGA SIKU-SIKU")
    else:
        print("SEGITIGA BUKAN SIKU-SIKU")
else:
    print("BUKAN SEGITIGA")
