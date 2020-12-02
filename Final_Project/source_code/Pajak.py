#Masuk ke menu pembayaran
#Pilih Pajak
#Heading : MENU PEMBAYARAN PAJAK
#Opsi cuman 1 : PBB (kanan)
#Klik PBB

def pajak(tahun):
    #Heading : SILAHKAN MASUKAN TAHUN FISKAL ANDA
    #User input tahun fiskal
    tahun = int(input("Tahun Fiskal anda? "))
    #Input selalu benar
    print("B or S")
    ans = input("Jawaban anda? ")
    if ans == "b" or ans == "B":
        #Next Page
        print("Benar")
        #Heading : 
        #PBB (PAJAK BUMI & BANGUNAN)
        #Tampilan
        #NOMOR PAJAK      : PENGKOMTRAVEL
        #NAMA             : 0102030405
        #KELURAHAN        : TUAN MOR
        #TAHUN FISKAL     : sesuai input (ans)
        #KODE PBB         : 23.57.030.002.011-0139.0 (formatnya)
        #JUMLAH           : Rp 201.406,00
        #ADM BANK         : BANK MANDIRI
        print("Y atau T ?") #Pilihan di kanan
        ans_2 = input("Jawaban anda: ")
        if ans_2 == "y" or ans_2 == "Y":
            print("Ya!")
            #Nextpage
            #Pop Up:
            #Tampilan:
            #TRANSAKSI ANDA TELAH SELESAI
            #APAKAH ANDA INGIN TRANSAKSI LAINNYA?
            #Ada 3 Opsi di Rata Kanan:
            #Pembayaran/Pembelian
            #Menu Utama
            #Selesai
            print("""PEMBAYARAN / PEMBELIAN 
                     MENU UTAMA
                     SELESAI""")
            #Misal Pembayaran = 1, Menu utama = 2, Selesai = 3
            ans_3 = input("Jawaban: ")
            if ans_3 == "1":
             #Mengarah ke menu pembayaran
                 print("PEMBAYARAN / PEMBELIAN")
            elif ans_3 == "2":
                 print("MENU UTAMA")
                 #Mengarah ke menu utama
            elif ans_3 == "3":
                 #Selesai, kartu keluar
                 print("SELESAI")
        elif ans_2 == "t" or ans_2 =="T":
            print("Transaksi dibatalkan")
            #Kartu keluar
            
    elif ans == "S" or ans == "s":
         print("Masukkan ulang")
        #Looping terus sampai benar
#Ada tombol <cancel> di setiap page untuk batal -> kartu keluar