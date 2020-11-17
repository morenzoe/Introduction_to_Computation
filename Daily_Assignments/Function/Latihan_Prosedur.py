# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 17 November 2020
# Kelas     	  : 16
# Deskripsi		  : Subprogram yang mencetak indeks dan isi array
                

# Latihan 5

# Program Cetak Array

# KAMUS GLOBAL
# N : integer
# T : array

#ALGORITMA
def CetakArray(jmlh, array):                                                    # fungsi CetakArray akan membutuhkan dua parameter    

  # KAMUS LOKAL PROSEDUR
  # jmlh  : integer
  # array : array

  # ALGORITMA PROSEDUR
  for i in range(jmlh):                                                         # melakukan perulangan sebanyak N
    print("["+str(i)+"] "+str(array[i]))                                        # cetak tiap indeks dan isi elemen

# ALGORITMA GLOBAL
N = int(input("Masukkan nilai N: "))                                            # deklarasi variabel N sebagai panjang array
T = [0 for i in range(N)]                                                       # deklarasi variabel T sebagai array

for i in range(N):                                                              # lakukan perulangan sebanyak N untuk mengisi array
  T[i]=int(input("Masukkan elemen ke-"+str(i)+": "))                            # isi elemen array sesuai dengan input pengguna

CetakArray(N, T)                                                                # jalankan fungsi CetakArray dengan parameter N dan T