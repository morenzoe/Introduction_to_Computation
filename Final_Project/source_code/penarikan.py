def penarikan(x):
  if x == 1:
    if int(db[id_g][3])>=300000:
      # next page
      # cek pin
      db[id_g][3]=str(int(db[id_g][3])-300000)
  elif x == 2:
    if int(db[id_g][3])>=500000:
      # next page
      # cek pin
      db[id_g][3]=str(int(db[id_g][3])-500000)
  elif x == 3:
    if int(db[id_g][3])>=1000000:
      # next page
      # cek pin
      db[id_g][3]=str(int(db[id_g][3])-1000000)
  elif x == 4:
    if int(db[id_g][3])>=1500000:
      # next page
      # cek pin
      db[id_g][3]=str(int(db[id_g][3])-1500000)
  elif x == 5:
    jmlh = int(input()) #jumlah sendiri
    if jmlh<=5000000 and jmlh%50000==0:
      if int(db[id_g][3])>=jmlh:
        # next page
        # cek pin
        db[id_g][3]=str(int(db[id_g][3])-jmlh)