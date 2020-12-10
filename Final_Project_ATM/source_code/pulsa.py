def pulsa(x, y):
  if x == 1: #pasca
    # next page
    # pilihan provider

    # next page
    # pilihan nominal pulsa
    
    if int(db[id_g][3])>=int(y)*50000:
      # next page
      # isi nomor
      nomor = input()
      if nomor[0:2] == "08":
        # next page
        # cek pin
        db[id_g][3]=str(int(db[id_g][3])-int(y)*50000)

  elif x == 2: #pra
    # next page
    # pilihan provider
    # next page
    # pilihan nominal pulsa

    if int(db[id_g][3])>=int(y)*50000:
      # next page
      # isi nomor
      nomor = input()
      if nomor[0:2] == "08":
        # next page
        # cek pin
        db[id_g][3]=str(int(db[id_g][3])-int(y)*50000)