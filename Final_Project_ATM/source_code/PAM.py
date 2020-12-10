# Tulisan di tengah atas: DAFTAR PAM
def pam(x):
    # User input nomor jenis PAM (x)
    # Looping biar lanjut terus
    if x == 1:
        print('PAM PALYJA')
        # Langsung next page
        # Tampilan next page:
        kode = int(input('Silahkan masukkan kode langganan Anda: '))
        # Asumsi kode langganan True
        print('(B/S)?')
        ans = input('Jawaban: ')
        if ans == 'B' or ans == 'b':
            print('Lanjut')
            # Langsung next page
        elif ans == 'S' or ans == 's':
            print('Silahkan masukkan ulang')
            # Ulang/loop ke input kode langganan
        else:
            print('Input salah, ulangi.')
            # Ulang/loop ke input Jawaban
        # Tekan <CANCEL> untuk batal (kartu keluar)

    elif x == 2:
        print('PAM TPJ')
        print('(Y/T)?')
        opsi = input('Jawaban:')
        if opsi == 'Y' or opsi == 'y':
            # Langsung next page
            # Tampilan next page:
            kode = int(input('Silahkan masukkan kode langganan Anda: '))
            # Asumsi kode langganan True
            print('(B/S)?')
            ans = input('Jawaban: ')
            if ans == 'B' or ans == 'b':
                print('Lanjut')
                # Langsung next page
            elif ans == 'S' or ans == 's':
                print('Silahkan masukkan ulang')
                # Ulang/loop ke input kode langganan
            else:
                print('Input salah, ulangi.')
                # Ulang/loop ke input Jawaban
            # Tekan <CANCEL> untuk batal (kartu keluar)
        elif opsi == 'T' or opsi == 't':
            print('Silahkan masukkan ulang')
            # Ulang/loop ke awal input x

    elif x == 3:
        print('PDAM KOTA BANDUNG')
        print('(Y/T)?')
        opsi = input('Jawaban:')
        if opsi == 'Y' or opsi == 'y':
                # Langsung next page
                # Tampilan next page:
            kode = int(input('Silahkan masukkan kode langganan Anda: '))
            # Asumsi kode langganan True
            print('(B/S)?')
            ans = input('Jawaban: ')
            if ans == 'B' or ans == 'b':
                print('Lanjut')
                # Langsung next page
            elif ans == 'S' or ans == 's':
                print('Silahkan masukkan ulang')
                # Ulang/loop ke input kode langganan
            else:
                print('Input salah, ulangi.')
                # Ulang/loop ke input Jawaban
            # Tekan <CANCEL> untuk batal (kartu keluar)
        elif opsi == 'T' or opsi == 't':
            print('Silahkan masukkan ulang')
            # Ulang/loop ke awal input x
    else:
        print('Input salah, ulangi.')
    # Tekan <CANCEL> untuk batal (kartu keluar)