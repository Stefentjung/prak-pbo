#Nama   : Stefen Tjung
#NIM    : 121140057

#Deklarasi Variabel
kesempatan = 1

#Perulangan untuk mengulang percobaan apabila Nama pengguna dan kata sandi salah
while kesempatan <= 3 :
    #Pengguna memasukan Nama pengguna dan kata sandi
    username=input("Masukan Nama Pengguna Anda  : ")
    paswword=input("Masukan Kata Sandi anda     : ")
    
    #Kasus Apabila Pengguna memasukan kata sandi yang benar makan sistem akan break dan berhenti
    if username=="informatika" and password=="12345678":
        print("Login Sucess!")
        break
    
    #Kasus apabila pengguna salah memasukan kata sandi maka akan berulang apabila lebih dari 3 kali
    #maka akan terblokir dan program berhenti.
    else:
        kesempatan = kesempatan + 1
        if kesempatan==4:
            print("Anda sudah mencoba lebih dari 3 kali, Akun Anda TERBLOKIR!")
        else:
            print("Nama pengguna dan Kata sandi anda tidak cocok!")
            
