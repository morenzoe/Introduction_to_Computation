def cekrek(rek):
  i=db_search(db, rek)
  if  i != None:
    return i
  elif  i == None:
    return None
  