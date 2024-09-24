#1 1 2 3 5 8 13 21

fibbonaci=[1,1]

for i in range(8):
    fibbonaci.append(fibbonaci[i]+fibbonaci[i+1])

print(fibbonaci)
