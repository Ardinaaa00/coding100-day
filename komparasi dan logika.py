#membuat gabungan area rentang dari angka

inputUser = float (input("masukkan angka yang bernilai kurang dari 3 lebih besar dari 10"))

#memeriksa angka kurang dari 3
isKurangDari =(inputUser < 3)
print("Kurang Dari 3 =",isKurangDari)

#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print ("Lebih Dari 10 ", isLebihDari)

isCorret = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorret)
