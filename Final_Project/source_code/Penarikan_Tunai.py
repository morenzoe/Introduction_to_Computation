#Menu : PENARIKAN TUNAI
""" Pas layar utama -> klik menu lainnya -> klik PENARIKAN TUNAI"""
#Heading: 
#           SILAHKAN MASUKAN JUMLAH PENARIKAN
#              DALAM KELIPATAN Rp. 50.0000
#          MAKSIMUM 1 KALI PENARIKAN 1.250.000
print("Silahkan Masukkan Jumlah Penarikan")
jum = int(input("Berapa? ")) #Jumlah nominal
if jum < "1250000":
    #Ada opsi Benar/Salah
    print("B/S? ")
    jawab = input("B or S? ")
    if jawab == "B" or jawab == "b":
        #Next Page
        print("Benar")
        #Uang keluar
        #Ada statement
        print("Silahkan Ambil Uang Anda")
    elif jawab == "S" or jawab == "s":
        #Jawaban kosong lagi, isi ulang
        print("Silahkan isi kembali nominal")
        #Looping sampai jawab == B
else:
    #Tidak bisa dilakukan
    print("Mohon maaf transaksi anda tidak bisa dilakukan")

