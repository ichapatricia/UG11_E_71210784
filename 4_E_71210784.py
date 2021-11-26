print("=======Program Test Aritmatika dasar=======")
print("Pilihan level yang tersedia: ")
print("1. Easy")
print("2. Medium")
print("3. Hard")
tingkat = int(input("Masukan tingkatan yang ingin anda coba: "))

if tingkat == 1: 
    print("Berapakah hasil dari 33 + 34")
    jawaban = 33 + 34
    jawab = int(input("Masukan jawaban anda: ")) 
    
    if jawab == jawaban: 
          print("Jawaban anda benar!")
else: 
        print("Jawaban anda salah!")

if tingkat == 2:
    print("Berapakah hasil dari 29/42*21")
    jawaban = 29/42*21
    jawab = float(input("Masukan jawaban anda: "))

    if jawab == jawaban: 
        print("Jawaban anda benar!")
else:
    print("Jawaban anda salah!")

if tingkat == 3:
    print("Berapakah hasil dari 83-31-83-33")
    jawaban = 83-31-83-33
    jawab = int(input("Masukan jawaban anda: "))

    if jawab == jawaban:
        print("Jawaban anda benar")
else:
    print("Jawaban anda salah")