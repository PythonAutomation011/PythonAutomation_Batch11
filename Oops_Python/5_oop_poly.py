

# class IPLCaptain2018:
#     def captain_name(self):
#         print('2018 MI -> Sachin')
#
# class IPLCaptain2023(IPLCaptain2018):
#     def captain_name(self):
#         super().captain_name()
#         print('2023 MI -> Rohit')
#
# i=IPLCaptain2023()
# i.captain_name()






















# class Cricket:
#     def __init__(self,TN):
#         self.TN=TN
#
#     def cricket_ipl_2024(self):
#         print(f'2024 year IPL :{self.TN}')
#
#     def cricket_ipl_2024(self):
#         print(f'2025 year IPL :{self.TN}')
#
#     def cricket_ipl_2024(self):
#         print(f'2026 year IPL :{self.TN}')
#
#
# c1=Cricket('MI')     #cricket
# c2=Cricket('CSK')
# c3=Cricket('DD')
# c4=Cricket('RR')
# c1.cricket_ipl_2024()
# c2.cricket_ipl_2024()
# c3.cricket_ipl_2024()
# c4.cricket_ipl_2024()
#
#
#
#
#
#
#
#







# class Employee:
#     def __init__(self,salary):
#         self.salary=salary
#     def __add__(self,other):
#         return self.salary+other.salary
#     def __sub__(self,other):
#         return self.salary-other.salary
#
# e1=Employee(10000)    #Employee     e1.salary=10000
# e2=Employee(30000)     #Employee    e2.salary=30000
# print(e1+e2)        #Employee+Employee----Not
# print(e1-e2)       #e1.salary-e2.salary













#
#
# class A:
#     def m1(self):
#         print('m1 of A class')
# class B:
#     def m1(self):
#         print('m1 of B class')
# class C:
#     def m1(self):
#         print('m1 of C class')
# class D:
#     def m1(self):
#         print('m1 of D class')
#
#
# def call_method_based_obj(obj):
#     obj.m1()
#
# l1=[A(),B(),C(),D()]   #sarv object created
#
# #A ---> method   B---method  C----method  D---method
# for i in l1:
#     print(type(i))
#     call_method_based_obj(i)   #A()  B()  C()  D()