import random

class Robot:
    jumlah_turn = 0
    
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage
        
    def lakukan_aksi(self):
        # Jika jumlah_turn kelipatan 3 dan robot ini Antares
        if self.jumlah_turn % 3 == 0 and isinstance(self, Antares):
            print(f"{self.nama} melakukan serangan kritis!")
            self.damage *= 1.5
        
        # Jika jumlah_turn kelipatan 2 dan robot ini Alphasetia
        if self.jumlah_turn % 2 == 0 and isinstance(self, Alphasetia):
            print(f"{self.nama} menambah darah sebanyak 4000 HP!")
            self.health += 4000
            
        # Jika jumlah_turn kelipatan 4 dan robot ini Lecalicus
        if self.jumlah_turn % 4 == 0 and isinstance(self, Lecalicus):
            print(f"{self.nama} melakukan serangan kritis dan menyembuhkan diri!")
            self.damage *= 2
            self.health += 7000
        
        # Menyerang robot lawan
        lawan = random.choice(opponent_list)
        print(f"{self.nama} menyerang {lawan.nama} sebanyak {self.damage} DMG!")
        lawan.terima_aksi(self.damage)
        
        # Menambah jumlah_turn
        self.jumlah_turn += 1
        
        # Cek apakah sudah waktunya menyembuhkan diri
        if self.jumlah_turn % 4 == 0 and isinstance(self, Alphasetia):
            print(f"{self.nama} menyembuhkan diri sebanyak 4000 HP!")
            self.health += 4000
        
    def terima_aksi(self, damage):
        self.health -= damage
        print(f"{self.nama} menerima serangan sebanyak {damage} DMG!")
        print(f"{self.nama} sisa darah: {self.health} HP\n")
        

class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)
        
        
class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)
        
        
class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)


# Main program
print("Selamat datang di pertandingan robot Yamako!")
robot_choice = input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")
if robot_choice == "1":
    robotmu = Antares()
elif robot_choice == "2":
    robotmu = Alphasetia()
elif robot_choice == "3":
    robotmu = Lecalicus()
else:
    print("Input tidak valid.")
    exit()

opponent_choice = input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")
if opponent_choice == "1":
    opponent = Antares()
elif opponent_choice == "2":
    opponent = Alphasetia()
elif opponent_choice == "3":
    opponent = Lecalicus()
else:
    print("Input tidak valid.")
    exit()

opponent_list = [opponent, robotmu]
