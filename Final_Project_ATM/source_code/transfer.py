def transfer(rek_t, jmlh):
  id_t = cekrek(rek_t) #cek rekening dulu sebelum pindah?
  
  if id_t != None:
    # next page
    if int(db[id_g][3])>=jmlh:
      # next page

      # konfirmasi
      # no rek tujuan v1 (rek_t)
      # nama v2 (db[id_t][0])
      # jumlah v3 (jmlh)
      # no rek v4 (db[id_g][1])
      db[id_g][3]=str(int(db[id_g][3])-jmlh)
      db[id_t][3]=str(int(db[id_t][3])+jmlh)
      #kode bank langsung aja tulis di js?
      
      # next page
      # cek pin