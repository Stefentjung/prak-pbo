#Nama : Stefen Tjung
#NIM  : 121140057
#Kelas: RB

class Data_diri :
    
    def __init__(self, nama, nim, kelas_pbo, jumlah_sks):
        self.nama=nama
        self.nim=nim
        self.kelas_pbo=kelas_pbo
        self.jumlah_sks=jumlah_sks

    def print_biodata(self):
        print(self.nama)
        print(self.nim)
        print(self.kelas_pbo)
        print(self.jumlah_sks)


nama=input("Masukan Nama :  ")
nim=input("Masukan NIM :  ")
kelas_pbo=input("Masukan Kelas PBO :  ")
jumlah_sks=input("Masukan Jumlah SKS :  ")

orang1= Data_diri(nama, nim, kelas_pbo, jumlah_sks)


orang1.print_biodata()

