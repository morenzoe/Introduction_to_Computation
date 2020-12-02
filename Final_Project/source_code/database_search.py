def db_search(db, val):
  for i in range(len(db)):
    try:
      db[i].index(val)
      id = i
      return id
    except ValueError:
      continue