def daftar(nama, tanggallahir,gender, asalsekolah, namaorangtua, agama, nomor, alamat):
   if gender=="perempuan":
      print("Selamat Datang di IE Nona "+nama +"Biodata kamu adalah sebagai berikut")
   print ("nama        :"+nama)
   print ("tgl         :"+tanggallahir)
   print ("asalsekolah :"+asalsekolah)
   print ("namaorangtua:"+namaorangtua )
   print ("agama       :"+agama)
   print ("nomor       :"+nomor)
   print ("alamat      :"+alamat)

# (nama, tanggallahir,gender, asalsekolah, namaorangtua, agama, nomor, alamat):
daftar("silgia", "11 maret 2006", 'perempuan',"sman1cicurug", "tia dan eko", "islam", "089676767089","cicurug")

def absensi(nama, tanggal):
   print("nama:"+ nama)
   print("tanggal:"+ tanggal)

absensi("im sol", "12")

def upgradelevel(name, score, lastlevel, nextlevel):
   print("nama:"+name)
   print("nilai:"+score)
   print("nilaiterakhir:"+lastlevel)
   print("nilaibaru:"+nextlevel)

upgradelevel("sunje","95","80","99")

#invoice spp
def invoicespp (nama, level):
    print("Nama             : "+nama)
    print("level            : "+level)
invoicespp ("im sol","4")

#check spp
def checkspp (nama):
    print("Nama             : "+nama)
checkspp("silgia")