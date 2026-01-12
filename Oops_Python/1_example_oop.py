from abc import ABC,abstractmethod
#------------ABSTRACTION--------
class Vehicle(ABC):
    '''
    Abtract class for all the type of vehicles
    '''
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.speed=0    #0
    @abstractmethod
    def start_enginee(self):
        pass
    @abstractmethod
    def stop_enginee(self):
        pass
    def set_speed(self,speed):   #setter
        '''set the speed for vehicle'''
        if speed>0:
            self.speed=speed
        else:
            print('speed cant be negative')
    def get_speed(self):    #getter
        print(f'speed is :{self.speed}')
        return self.speed

class Car(Vehicle):     #iheritance---single
    def start_enginee(self):
        print(f'{self.brand}:{self.model} can start')
        self.speed=15    #override
        print(f'speed: {self.speed}')
    def stop_enginee(self):
        print(f'{self.brand}:{self.model} can stop')
        self.speed = 0  # override
        print(f'speed: {self.speed}')

class Bike(Vehicle):     #iheritance---single
    def start_enginee(self):
        print(f'{self.brand}:{self.model} can start')
        self.speed=3    #override
    def stop_enginee(self):
        print(f'{self.brand}:{self.model} can stop')
        self.speed = 0  # override

#poly---ducktyping
def vehicle_test(obj):
    print('start engineer of')
    obj.start_enginee()
    print('speed of enginee')
    obj.get_speed()
    obj.set_speed(15)
    obj.stop_enginee()

c1=Car('TATA','Altroz')
b1=Bike('Honda','XYZ')
n=input('enter the choice 1 or 2')
if n==1:
    vehicle_test(c1)
else:
    vehicle_test(b1)