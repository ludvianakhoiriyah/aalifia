# =========================
# suhu.py
# Modul konversi suhu
# =========================

def konversi_suhu(nilai, dari, ke):
  nilai = float(nilai)

  dari = dari.lower()
  ke = ke.lower()

  if dari not in ['c','f','k']:
    return "Eror: satuan asal tidak valid, gunakann C, F, atau K"
  
  if ke not in ['c','f','k']:
    return "Eror: satuan tujuan tidak valid, gunakann C, F, atau K" 

  if dari == 'c':
    if ke == 'f':
      return hasil = nilai * 9/5 + 32
    elif ke == 'k':
      return hasil = nilai + 273.15
    else:
      return hasil = nilai

  if dari == 'f':
    if ke == 'c':
      return hasil = (nilai - 32) * 5/9
    elif ke == 'k':
      return hasil = (nilai - 32) * 5/9 + 273.15
    else:
      return hasil = nilai

  if dari == 'k':
    if ke == 'c':
      return hasil = nilai - 273.15
    elif ke == 'f':
      return hasil = (nilai - 273.15) * 9/5 + 32
    else:
      return hasil = nilai 

  if ke == 'k' and hasil < 0:
    return "Eror: nilai suhu tidak valid"

return hasil
