# Program SuhuKotaBandung
# Analisis data suhu kota bandung

# KAMUS
# suhu : array [0..29] of float
# sum, mean, min : float
# i, tanggal: int
# found : bool; menentukan X sdh ditemukan/belum

# ALGORITMA
N = 5
suhu = [0 for i in range(N)]

for i in range(N):
    suhu[i] = float(input(f"Masukkan suhu tanggal ke-{i+1}: "))

sum = 0
for i in range(N):
    sum += suhu[i]
mean = sum / N
print("Rata-rata suhu kota Bandung di bulan Sept 2018:", mean)

min = suhu[0]
for i in range(1, N):
    if suhu[i] < min:
        min = suhu[i]
print("Suhu terendah di bulan Sept. 2018:", min)

print("Tanggal berikut >= 30 derajat:")
for i in range(N):
    if suhu[i] >= 30:
        print("Tanggal", i+1, ":", suhu[i])

# Pencarian dimulai dari elemen ke-0
i = 0
found = False # found = False; X belum ditemukan
tanggal = 0
while (i < N and found == False):
    if (suhu[i] < 15):
        found = True # found = True; X sudah ditemukan
        tanggal = i+1
    else:
        i = i + 1 # hanya increment jika X belum ditemukan
# i = N-1 atau found = True
# Cetak Hasil
if (found == True): # X ditemukan di T
    print ("Tanggal", tanggal, "mempunyai suhu dibawah 15 derajat celcius [", suhu[tanggal-1], "derajat celcius ]")
else: # found = False; X tidak ditemukan di T
    print ("Suhu tidak pernah di bawah 15 derajat Celcius")
