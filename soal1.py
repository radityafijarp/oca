harga_pokok=int(input("Masukan Harga Pokok: "))
harga_jual=int(input("Masukan Harga Jual: "))

profit=harga_jual-harga_pokok
percet_profit=profit/harga_pokok*100

formatted_percent_profit = "{:.2f}".format(percet_profit)+"%"
print(formatted_percent_profit)