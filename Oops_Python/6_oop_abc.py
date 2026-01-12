from abc import ABC,abstractmethod
#define contracts
class Employee(ABC):
    @abstractmethod
    def m1(self):
        pass


class B(Employee):
    def m1(self):
        print('this is m1')

class C(Employee):
    def m1(self):
        l1=[10,20,30,40]
        for i in range(len(l1)):
            print(i)

b1=C()
b1.m1()