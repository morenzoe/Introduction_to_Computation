#Menu utama-> Klik menu lainnya->Klik Q-pay
#Tampilan yang muncul :
#SILAHKAN MASUKKAN KODE BILLING ANDA (center)
#User masukin kode billing di text box
def qpay(kode):
    kode_def = "0102030405"  #Kode default
    if kode == kode_def:
        jawab = input("B / S ? ") #Bener or Salah
        if jawab == "B" or jawab == "b":
        #Langsung next page
        #Tampilan: 
        #KONFIRMASI PEMBAYARAN (center)
        #PEMBAYARAN  : PENGKOMTRAVEL
        #KODE BILLING: 0102030405
        #NAMA        : TUAN MOR
        #NO.TELP     : 02152913584
        #JUMLAH BAYAR: Rp 506.000,00
        #Keterangan  : TIKET JAKARTA - BANDUNG
        #              UNTUK 2 ORANG
        #              PULANG PERGI
        #              RESERVASI & DELIVERY ADALAH TANGGUNG JAWAB PANTRAVEL
            print("Y/T ?")
            jawab_2 = input("Jawaban : ")
            if jawab_2 == "Y" or jawab_2 == "y": #pilih Ya
                #Next Page
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
                jawab_3 = input("Jawaban: ")
                if jawab_3 == "1":
                    #Mengarah ke menu pembayaran
                    print("PEMBAYARAN / PEMBELIAN")
                elif jawab_3 == "2":
                    #Mengarah ke menu utama
                    print("MENU UTAMA")
                elif jawab_3 == "3":
                    #Selesai, kartu keluar
                    print("SELESAI")
            elif jawab_2 == "T" or jawab == "t": #Pilih Tidak
                print("Transaksi dibatalkan") #Pembatalan, kartu keluar
        elif jawab == "S" or jawab == "s":
            print("Silahkan Masukkan ulang")
            #Jika salah maka isi ulang kode billing
            #looping terus sampe bener
    elif kode != kode_def:
        print("Kode yang anda masukkan salah, Masukkan ulang")
        #Diminta untuk masukkin kode billing ulang
        
#Ada tombol <cancel> di setiap page untuk batal -> kartu keluar
 