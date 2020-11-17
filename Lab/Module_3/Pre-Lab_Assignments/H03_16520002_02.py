# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 17 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang memeriksa apakah semua isi array B ada di
#                 array A dan sebaliknya

# Soal 2

# Program 

#KAMUS
# NA, NB, Max, Min : integer
# A, B, FA, FB : array
# t1, t2, lanjut : boolean

#ALGORITMA
NA = int(input("Masukkan banyaknya elemen A: "))                                # buat variabel untuk menyimpan jumlah elemen A dari input integer

A = [0 for i in range(NA)]                                                      # deklarasi variabel array berisi angka 0 sebanyak NA

for i in range(NA):                                                             # lakukan perulangan sebanyak N kali
  A[i] = int(input("Masukkan elemen A ke-"+str(i+1)+": "))                      # ganti isi array A ke-i dengan input, asumsi input adalah integer

NB = int(input("Masukkan banyaknya elemen B: "))                                # buat variabel untuk menyimpan jumlah elemen B dari input integer

B = [0 for i in range(NB)]                                                      # deklarasi variabel array berisi angka 0 sebanyak NB

for i in range(NB):                                                             # lakukan perulangan sebanyak N kali
  B[i] = int(input("Masukkan elemen B ke-"+str(i+1)+": "))                      # ganti isi array B ke-i dengan input, asumsi input adalah integer

if NA != NB:                                                                    # jika jumlah elemen array A dan B berbeda, pasti bukan anagram
  print("B bukan anagram dari A")
else:                                                                           # jika jumlah elemen sama, buat tabel frekuensi
  Max = 0                                                                       # tabel frekuensi untuk semua angka dari terkecil hingga terbesar
  Min = 0
  
  for i in range(NA):                                                           # memeriksa semua elemen array untuk mencari nilai maksimum dan minimum 
    if A[i] > Max:                                                              # jika anagram, nilai maksimum dan minimum array A sama dengan array B, cukup periksa salah satu saja
      Max = A[i]
    elif A[i] < Min:
      Min = A[i]

  t1 = True                                                                     # inisiasi kriteria untuk melanjutkan program
  t2 = True
 
  for i in range(NB):                                                           # periksa seluruh isi array B
    if B[i] > Max:                                                              # jika ada nilai di array B yang lebih besar dari Max, tidak lanjut
      t1 = False
    if B[i] < Min:                                                              # jika ada nilai di array B yang lebih kecil dari Min, tidak lanjut
      t2 = False
  
  lanjut = t1 and t2                                                            # kriteria melanjutkan program

  if lanjut==True:
    FA = [0 for i in range(Min, Max+1)]                                         # buat variabel array untuk menampung frekuensi seluruh angka dari Min sampai Max
    FB = [0 for i in range(Min, Max+1)]

    for i in range(Min, Max+1):                                                 # periksa semua angka dari Min sampai Max
      for j in range(NA):       
        if i == A[j]:                                                           # bandingkan dengan semua elemen array A
          FA[i-abs(Min)] = FA[i-abs(Min)] + 1                                   # tambahkan 1 pada elemen frekuensi masing-masing untuk setiap elemen array A yang sama dengan angka uji
        if i == B[j]:                                                           # bandingkan dengan semua elemen array B
          FB[i-abs(Min)] = FB[i-abs(Min)] + 1
    
    if FA == FB:                                                                # jika tabel frekuensi sama, B adalah anagram A
      print("B adalah anagram dari A")                                          # asumsi dua array kosong adalah anagram
    else:                                                                       # jika tabel frekuensi beda, B bukan anagram A
      print("B bukan anagram dari A")

  else:                                                                         # jika nilai maksimum atau minimum tidak sesuai, pasti bukan anagram
    print("B bukan anagram dari A")                                         