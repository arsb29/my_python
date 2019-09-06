import random

class Player:
    def __init__ (self, new_name='Игрок без имени',hp=100):
        self.name = new_name
        self.hp=hp
        self.distance=0
        self.damage=3
        
        print(self.name,'(',self.hp,'%)',"- присоединился к серверу!")
    def set_name(self,new_name):
        self.name = new_name

    def get_info(self):
        print()
        print('Информация об игроке',self.name)
        print('HP',self.hp,'%')
        print('Урон -',self.damage)
        print('Дистанция',self.distance)
        print()

    def attack(self,self2):
        self2.hp-=self.damage
        self.hp+=1
        print('Игрок',self.name,'(',self.hp,'%)',' → ',self2.name,'(',self2.hp,'%)')

    def run(self,meters):
        self.distance+=meters
        self.hp-=round(meters*0.1)
        print(self.name,'(',self.hp,'%)',' пробежал',meters,'метров. Всего:',self.distance,'метров.')

    def pick(self):
        random_number = random.choice(['attack1','hp1'])
        if random_number=='attack1':
            self.damage+=1
            print(self.name,'(',self.hp,'%) собрал улучшение для атаки. Урон от',self.name,'-',self.damage)
        if random_number=='hp1':
            self.hp+=5
            print(self.name,'(',self.hp,'%) подобрал аптечку.')

    
    
class Flyer(Player):

        
    def fly(self,meters):
        self.distance+=meters
        self.hp-=round(meters*0.05)
        print(self.name,'(',self.hp,'%)',' пролетел',meters,'метров. Всего:',self.distance,'метров.')
    

p1=Player("Настя")
p2=Player("Сеня")
p2.pick()
p1.attack(p2)
p2.run(150)
p2.run(450)
p1.pick()
p1.attack(p2)
p1.run(160)
p3=Flyer("Альберт")
p3.run(250)
p3.fly(250)
p2.pick()
p1.attack(p3)
p1.run(340)
p2.get_info()
