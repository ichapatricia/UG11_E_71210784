def bilangan_kuadrat(): 
    hasil = bilangan ** 2
    return hasil 
def bilangan_akar():
    hasil = bilangan ** 0.5 
    return hasil

print("Menu program yang Tersedia")
print("1. Pangkatkan angka ")
print("2. akarkan bilangan")
angka = int(input("Masukan pilihan yang diinginkan: "))
if angka == 1:
    print("Masukan angka yang ingin anda pangkatkan")
    bilangan= float(input("angka: "))
    print("Ingin modifikasi angka pangkat YES/NO")
    modifikasi = str(input(":"))
if modifikasi== "YES":
    baru= int(input("Masukan nilai pangkat:"))
    print("Hasil dari", bilangan, "^", baru , "=", bilangan_kuadrat())
    
    if modifikasi== "NO": 
        print("Hasil dari", bilangan , "^2" , "=" , bilangan_akar(bilangan,2))

if angka == 2:
    print("Masukan angka yang ingin diakar")
    bilangan= float(input("angka: "))
    print("Ingin modifikasi akar YES/NO")
    modifikasi= str(input(":"))

if modifikasi == "YES":
     baru= float(input("Masukkan nilai akar:"))
     print("Hasil akar pangkat", baru,"dari", bilangan,"=", bilangan_akar())
if modifikasi == "NO":
    print("Hasil akar pangkat", angka, "dari", bilangan, "=")
