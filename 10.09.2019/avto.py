class Client():

    
    def __init__(self,
                 name = "Клиент без имени",
                 adress = "Нет адреса",
                 number= "8XXXXXXXXXX"):
        self.name = name
        self.adress = adress
        self.number = number

    def set_name(self, name):
        self.name = name

    def set_adress(self,adress):
        self.adress = adress

    def set_number(self, number):
        self.number = number
    
    def get_info(self):
        print('\nИнформация о клиенте')
        print('Имя:',self.name,'\nАдрес:',self.adress,'\nТелефон:',self.number)


class Car():

    def __init__(self,
          brand = 'AAA',
          model = 'ZZZ',
          year = 'YYYY',
          owner = ''):
        self.brand = brand
        self.model = model
        self.year = year
        

    def set_brand(self, brand):
        self.brand = brand

    def set_adress(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def get_info(self):
        print('\nИнформация по автомобилю:')
        print('Бренд:',self.brand,'\nМодель:',self.model,'\nГод выпуска:',self.year)

    def set_owner(self, owner):
        self.owner = owner
        owner.car = self
        print(f"\nМашина клиента {owner.name} - {self.brand}")

class Worker():

    def __init__(self, name, savings):
        self.name = name
        self.savings = savings
        print(f'\nВ автомастерской новый сотрудник - {self.name}')

class Order():

    def __init__(self, client, worker):
        worker.client = client
        client.worker = worker
        worker.order = self
        self.worker = worker
        self.client = client
        print(f'\nВ автомастерскую поступил заказ. С клиентом {client.name} работает {worker.name}')

class Inspection():

    def __init__(self, order, trouble, cost):
        self.trouble = trouble
        self.worker = order.worker
        self.cost = cost
        print(f"\nПосле осмотра автомобиля (владелец - {order.client.name}) "
              f"менеджер {self.worker.name} "
              f"\nвыявил неисправность в следующей детали: {trouble}"
              f"\nремонт автомобиля {order.client.car.brand} будет стоить {cost} долларов")

class Payment():
    
    def __init__(self,inspection):
        inspection.worker.savings += int(inspection.cost)*0.35
        print(f"\nПроизводится оплата клиентом {inspection.worker.client.name} в размере {inspection.cost} долларов."
              f"\nПосле выполнения всех работ менеджер заработает 35%, то есть {int(inspection.cost)*0.35} долларов"
              f"\nСбережения менеджера - {inspection.worker.name} равны {inspection.worker.savings} долларам")
    

    
client1 = Client('Настя','Невский проспект д.25','89805552502')
client1.get_info()

car1 = Car('Porsche','Dambo','2018')
car1.get_info()

car1.set_owner(client1)

worker1 = Worker('Лионель',100)

order1 = Order(client1, worker1)

tr1 = Inspection(order1,'Мотор',100)

pay1 = Payment(tr1)

client2 = Client('Арсений','Лиговский проспект д.29', '89115552902')
client2.get_info()

car2 = Car('BMW','Zver','2019')
car2.get_info()

car2.set_owner(client2)

worker2 = Worker('Оливер',55)

order2 = Order(client2, worker2)

tr2 = Inspection(order2,'Подвеска',561)

pay2 = Payment(tr2)
