print("====== Program Manipulasi String ======")
print("Pilihan Menu: ")
print("1. Hitung kata")
print("2. Cek kata")
print("3. Ubah kata")

pilih = str(input("Pilihan anda: "))
kalimat = str(input("Masukan sebuah kalimat/kata : "))
hasil = (kalimat.lower())

if pilih == '1': 
    b = input("Masukan kata yang ingin dihitung: ")
    t = hasil.count(b)
    print("Terdapat sebanyak", t, "kata", b, "didalam string")

if pilih == '2':
    b = input("Masukan kata yang ingin di cek: ")
    t = b.upper()
    s = hasil.replace(b,t)
    print("kata", b,"terdapat dalam string", )
    print("string diubah menjadi:")
    print(s)

if pilih == '3':
    b = input("Masukan kata yang ingin diubah: ")
    f = input("Masukan kata pengganti: ")
    print("Anda akan mengubah kata", b, "menjadi", f, "sebanyak 1x")
    ganti = str(input("Apakah anda ingin mengubah jumlah total pengganti kata?(yes/no) : "))

if ganti == "yes":
    h = int(input("Masukan jumlah total pengganti: "))
    print("String berhasil diubah menjadi: ")
    u = hasil.replace(b ,f ,h )
    print(u)

elif ganti == "no":
    h = 1
    print("String berhasil diubah menjadi: ")
    u = hasil.replace(b,f,h)
    print(u)




