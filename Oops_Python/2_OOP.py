#car----> attribute----variable---> brand,model,year,colour,door
#action----> methods---->start engineer,stop engineer

class Car:
    def __init__(self,brand,model,year,colour,door=4):
        self.brand=brand
        self.model=model
        self.year=year
        self.colour=colour
        self.door=door
    def __str__(self):
        return f'{self.brand}-{self.model}-{self.year}-{self.colour}-{self.door}'

    def __repr__(self):
        return str(self)

    def start_enginee(self):  #self keyword ----> instance method
        print(f'The {self.model} is start')

    def stop_enginee(self):
        print(f'The {self.model} is stopped')

    @classmethod
    def name_of_enginee(cls):
        print(f'this is class method')

    @staticmethod
    def m1():
        print(10+10)


c1=Car('TATA','PUNCH',2025,'BLACK')  #position
c2=Car(brand='TOYOTA',model='COROLLA',year=2022,colour='white',door=4) #keywordbase
# c1.start_enginee()
# c1.stop_enginee()
# c2.start_enginee()
# c2.stop_enginee()
# c1.name_of_enginee()
# c2.name_of_enginee()
c1.m1()
c2.m1()
# l1=[c1,c2]
# print(l1)
#
# l2=[]
# l2.append(c1.brand)
# print(l2)