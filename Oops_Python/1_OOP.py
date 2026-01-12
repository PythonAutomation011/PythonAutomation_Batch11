class Teachear:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __str__(self):
        return f'{self.name},{self.age},{self.salary}'
    def __repr__(self):
        return str(self)
t1=Teachear(name='VB',age=22,salary=40000)
t2=Teachear(name='ABC',age=40,salary=10000)
t3=Teachear(name='MR.XYZ',age=31,salary=20000)
t4=Teachear(name='Mr.VY',age=35,salary=30000)
t5=Teachear(name='MR.CCC',age=21,salary=25000)
t6=Teachear(name='ABC',age=40,salary=35000)
t7=Teachear(name='MR.PATIl',age=31,salary=70000)
t8=Teachear(name='Mr.RAM',age=40,salary=150000)
l1=[t1,t2,t3,t4,t5,t6,t7,t8]
print(l1)
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i].salary>l1[j].salary:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)








# class Employee:
#     def __init__(self,eid,ename,ecity):
#         self.e_id=eid
#         self.ename=ename
#         self.ecity=ecity
#     def __str__(self):
#         return f'EID:{self.e_id},ENAME:{self.ename},ECITY:{self.ecity}'
#     def __repr__(self):
#         return str(self)
#
# e1=Employee(101,'Vb','PUNE')
# e2=Employee(202,'ABC','mumbai')
# e3=Employee(303,'XYZ','banglore')
# l1= [e1,e2,e3]
# for i in range(len(l1)):
#     print(l1[i].e_id,l1[i].ename)

#can you all the ids of employeer















# class Resto:
#     def __init__(self,oid,cn,items,total_price):
#         self.orderid=oid
#         self.c_name=cn
#         self.items=items
#         self.total_price=total_price
#     def add_items(self):
#         l1=['starter']
#         for i in self.items:
#             l1.append(i)
#         print(l1)
#
# r1=Resto(oid=101,cn='VB',items=['VEG','NONVE'],total_price=500)
# r2=Resto(oid=102,cn='ABC',items=['NONVE'],total_price=500)
# r1.add_items()
# r2.add_items()
































# class SmartPhone:
#     def __init__(self,brand='SAM',model='s24',battery_life=24,price=10000):
#         self.brand=brand
#         self.model=model
#         self.battery_life=battery_life
#         self.price=price
#         print(f'{self.brand,self.model,self.battery_life}')
#
# s1=SmartPhone(brand='SAM',model='S24',battery_life=24,price=40000)
# s2=SmartPhone('IPHONE','15',24,3000)
# s3=SmartPhone('NOKIA','2201',12,5000)
# s4=SmartPhone()















# class Calculator:
#     def __init__(vaibhav,x,y):
#         vaibhav.x=x
#         vaibhav.y=y
#     def add_Two(vaibhav):
#         print(f'addition of {vaibhav.x,vaibhav.y} is {vaibhav.x+vaibhav.y}')
#     def sub_two(vaibhav):
#         print(vaibhav.x-vaibhav.y)
#
# a1=Calculator(10,20)   #self=a1 , x=10 y=20
# a1.add_Two()
# a2=Calculator(5,2)
# a2.add_Two()
# a1.sub_two()
# a2.sub_two()




























#
# class Employee:
#     def __init__(self):   #all variable initialise
#         self.name='VB'   #default
#         self.add='Pune'
#     def print_data(self):
#         print(self.name,self.add)
#
# a1=Employee()   #call the constructor
# a1.print_data()
