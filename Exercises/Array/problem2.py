N = int(input("Masukkan banyaknya element: "))
A = [0 for i in range(N)]
B = [0 for i in range(N)]

print("Elemen A:")
for i in range(N):
    A[i] = int(input())

print("Elemen B:")
for i in range(N):
    B[i] = int(input())

# A dan B harus deret bilangan, deret aritmatika
# A dan B bedanya harus sama

isDeret = True
bedaA = A[1] - A[0]
for i in range(2, N):
    bedaAnext = A[i] - A[i-1] 
    if bedaA != bedaAnext:
        isDeret = False
    else:
        bedaA = bedaAnext

bedaB = B[1] - B[0]
for i in range(2, N):
    bedaBnext = B[i] - B[i-1] 
    if bedaB != bedaBnext:
        isDeret = False
    else:
        bedaB = bedaBnext

if isDeret == True and bedaA == bedaB:
    print("A dan B merupakan double magic sequence.")
else:
    print("A dan B bukan merupakan double magic sequence.")