# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 18 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang memeriksa apakah suatu kata dibaca dengan cara yang sama
#                 meskipun dibalik

# Soal 3

# Program 

#KAMUS
#  : integer
#  : string
#  : list

#ALGORITMA
N = int(input("Masukkan panjang string: "))                                     # deklarasi variabel N untuk panjang string, asumsi N>0

M = input("Masukkan string: ")                                                  # deklarasi variabel M untuk string, asumsi len(M)==N

maks = 0                                                                        # deklarasi variabel maks untuk panjang string palindrom maksimum
for i in range(2,N+1):                                                          # cek setiap kemungkinan substring
  n=0
  while n+i<=N:
    tes = M[n:n+i]
    if tes == tes[::-1]:
      maks = i                                                                  # jika substring adalah palindrom, assing variabel maks sebagai panjang substring tersebut
    n+=1

print("Panjangnya adalah "+str(maks))                                           # cetak panjang substring maksimum