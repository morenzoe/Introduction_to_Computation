# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 02 Desember 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang menghitung nilai suatu fungsi matematika

# Soal 1

# Program Fungsi x

# KAMUS
# A, B : integer

# definisi fungsi f(x)
def fun_mat(x):
  # KAMUS LOKAL
  # fx : integer

  # ALGORITMA
  fx = x*x - 2*x + 5                                                            # menghasilkan nilai sesuai fungsi matematika f(x) = x^2 - 2x +5
  return fx                                                                     # mengembalikan hasil perhitungan

# ALGORITMA
A = int(input("Masukkan A: "))                                                  # menerima input batas bawah fungsi, asumsi A integer
B = int(input("Masukkan B: "))                                                  # menerima input batas atas fungsi, asumsi B integer dan B>=A

for i in range(A,B+1):
  print("f("+str(i)+") = "+str(fun_mat(i)))                                     # mencetak fungsi tertentu dan hasilnya