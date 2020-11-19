# Program HitungKelulusan
# Mencari jumlah lulus/tidak lulus berdasarkan nilai

# KAMUS
# Nilai : array [0..4] of char
# X, Lulus, TidakLulus : int

# ALGORITMA
Nilai = ['*' for i in range(5)]
Lulus = 0
TidakLulus = 0

for i in range(5):
    Nilai[i] = input("Nilai ke-" + str(i+1) + ": ")

for i in range(5):
    if Nilai[i] == "A" or Nilai[i] == "B" or Nilai[i] == "C":
        Lulus += 1
    else:
        TidakLulus += 1

print("Lulus:", Lulus)
print("Tidak Lulus:", TidakLulus)
