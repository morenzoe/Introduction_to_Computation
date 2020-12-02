# Tulisan di tengah atas: SILAHKAN PILIH PEMBAYARAN JENIS TIKET
# Muncul pilihan [1] PESAWAT UDARA dan [2] KERETA API
def tiket(tombol):
    # Tombol pilihan rata kanan
    # Misal tombol atas     = 1
    # Misal tombol bawah    = 2
    if tombol == 1:
        # Langsung next page
        # Tulisan di tengah atas: PEMBAYARAN TIKET
        # Muncul pilihan [1] GARUDA, [2] ADAM AIR, [3] RIAU AIR, [4] AIR ASIA, dan [5] AIR EFATA
        print('PESAWAT UDARA')
        x = int(input('Masukkan nomor urut penyedia tiket: '))
        # Tekan <CANCEL> untuk batal (kartu keluar)
        if x == 1:
            print('GARUDA')
            print('(Y/T)?')
            opsi = input('Jawaban: ')
            # Tekan <CANCEL> untuk batal (kartu keluar)
            if opsi == 'Y' or opsi == 'y':
                # Langsung next page
                # Tampilan next page:
                # Tulisan di tengah atas: SILAHKAN MASUKKAN KODE PEMESANAN ANDA
                kode = int(input('Masukkan kode pemesanan Anda: '))
                # Asumsi kode pemesanan True
                print('(B/S)')
                ans = input('Jawaban: ')
                # Tekan <CANCEL> untuk batal (kartu keluar)
                if ans == 'B' or ans == 'b':
                    print('Lanjut')
                    # Langsung next page
                elif ans == 'S' or ans == 's':
                    print('Silahkan masukkan ulang')
                    # Ulang/loop ke input kode pemesanan
                else:
                    print('Input salah, ulangi')
                    # Ulang/loop ke input Jawaban (ans)
            elif opsi == 'T' or opsi == 't':
                print('Silahkan pilih ulang')
                # Ulang/loop ke input nomor urut penyedia tiket (x)
                # Balik ke previous page
            else:
                print('Input salah, ulangi')
                # Ulang/loop ke input Jawaban (opsi)

        elif x == 2:
            print('ADAM AIR')
            print('(Y/T)?')
            opsi = input('Jawaban: ')
            # Tekan <CANCEL> untuk batal (kartu keluar)
            if opsi == 'Y' or opsi == 'y':
                # Langsung next page
                # Tampilan next page:
                # Tulisan di tengah atas: SILAHKAN MASUKKAN KODE PEMESANAN ANDA
                kode = int(input('Masukkan kode pemesanan Anda: '))
                # Asumsi kode pemesanan True
                print('(B/S)')
                ans = input('Jawaban: ')
                # Tekan <CANCEL> untuk batal (kartu keluar)
                if ans == 'B' or ans == 'b':
                    print('Lanjut')
                    # Langsung next page
                elif ans == 'S' or ans == 's':
                    print('Silahkan masukkan ulang')
                    # Ulang/loop ke input kode pemesanan
                else:
                    print('Input salah, ulangi')
                    # Ulang/loop ke input Jawaban (ans)
            elif opsi == 'T' or opsi == 't':
                    print('Silahkan pilih ulang')
                # Ulang/loop ke input nomor urut penyedia tiket (x)
                # Balik ke previous page
            else:
                print('Input salah, ulangi')
                # Ulang/loop ke input Jawaban (opsi)

        elif x == 3:
            print('RIAU AIR')
            print('(Y/T)?')
            opsi = input('Jawaban: ')
            # Tekan <CANCEL> untuk batal (kartu keluar)
            if opsi == 'Y' or opsi == 'y':
                # Langsung next page
                # Tampilan next page:
                # Tulisan di tengah atas: SILAHKAN MASUKKAN KODE PEMESANAN ANDA
                kode = int(input('Masukkan kode pemesanan Anda: '))
                # Asumsi kode pemesanan True
                print('(B/S)')
                ans = input('Jawaban: ')
                # Tekan <CANCEL> untuk batal (kartu keluar)
                if ans == 'B' or ans == 'b':
                    print('Lanjut')
                    # Langsung next page
                elif ans == 'S' or ans == 's':
                    print('Silahkan masukkan ulang')
                    # Ulang/loop ke input kode pemesanan
                else:
                    print('Input salah, ulangi')
                    # Ulang/loop ke input Jawaban (ans)
            elif opsi == 'T' or opsi == 't':
                    print('Silahkan pilih ulang')
                # Ulang/loop ke input nomor urut penyedia tiket (x)
                # Balik ke previous page
            else:
                print('Input salah, ulangi')
                # Ulang/loop ke input Jawaban (opsi)

        elif x == 4:
            print('AIR ASIA')
            print('(Y/T)?')
            opsi = input('Jawaban: ')
            # Tekan <CANCEL> untuk batal (kartu keluar)
            if opsi == 'Y' or opsi == 'y':
                # Langsung next page
                # Tampilan next page:
                # Tulisan di tengah atas: SILAHKAN MASUKKAN KODE PEMESANAN ANDA
                kode = int(input('Masukkan kode pemesanan Anda: '))
                # Asumsi kode pemesanan True
                print('(B/S)')
                ans = input('Jawaban: ')
                # Tekan <CANCEL> untuk batal (kartu keluar)
                if ans == 'B' or ans == 'b':
                    print('Lanjut')
                    # Langsung next page
                elif ans == 'S' or ans == 's':
                    print('Silahkan masukkan ulang')
                    # Ulang/loop ke input kode pemesanan
                else:
                    print('Input salah, ulangi')
                    # Ulang/loop ke input Jawaban (ans)
            elif opsi == 'T' or opsi == 't':
                    print('Silahkan pilih ulang')
                # Ulang/loop ke input nomor urut penyedia tiket (x)
                # Balik ke previous page
            else:
                print('Input salah, ulangi')
                # Ulang/loop ke input Jawaban (opsi)

        elif x == 5:
            print('AIR EFATA')
            print('(Y/T)?')
            opsi = input('Jawaban: ')
            # Tekan <CANCEL> untuk batal (kartu keluar)
            if opsi == 'Y' or opsi == 'y':
                # Langsung next page
                # Tampilan next page:
                # Tulisan di tengah atas: SILAHKAN MASUKKAN KODE PEMESANAN ANDA
                kode = int(input('Masukkan kode pemesanan Anda: '))
                # Asumsi kode pemesanan True
                print('(B/S)')
                ans = input('Jawaban: ')
                # Tekan <CANCEL> untuk batal (kartu keluar)
                if ans == 'B' or ans == 'b':
                    print('Lanjut')
                    # Langsung next page
                elif ans == 'S' or ans == 's':
                    print('Silahkan masukkan ulang')
                    # Ulang/loop ke input kode pemesanan
                else:
                    print('Input salah, ulangi')
                    # Ulang/loop ke input Jawaban (ans)
            elif opsi == 'T' or opsi == 't':
                    print('Silahkan pilih ulang')
                # Ulang/loop ke input nomor urut penyedia tiket (x)
                # Balik ke previous page
            else:
                print('Input salah, ulangi')
                # Ulang/loop ke input Jawaban (opsi)

        else:
            print('Input salah, ulangi')
            # Ulang/loop ke input nomor urut penyedeia tiket (x)

    elif tombol == 2:
        # Tulisan di tengah atas: SILAHKAN MASUKKAN KODE PEMBAYARAN ANDA
        print('KERETA API')
        kode = int(input('Masukkan kode pembayaran: '))
        # Asumsi kode pembayaran True
        print('(B/S)')
        ans = input('Jawaban: ')
        # Tekan <CANCEL> untuk batal (kartu keluar)
        if ans == 'B' or ans == 'b':
            print('Lanjut')
            # Langsung next page
        elif ans == 'S' or ans == 's':
            print('Silahkan masukkan ulang')
            # Ulang/loop ke input kode pembayaran
        else:
            print('Input salah, ulangi')
            # Ulang/loop ke input Jawaban (ans)