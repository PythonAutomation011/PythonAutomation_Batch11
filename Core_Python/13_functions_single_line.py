#lambda function----single function in python
#nameless function----> anonymous function
#no return
#no def keyword

#map,filter,reduce
# def add_two(a,b):
#     return a+b

#syntax----> lambda args:experession


# def add_two(a,b):
#     return a+b
#
# s=lambda x,y:x+y
# print(s(10,20))
# print(add_two(10,20))

# s=lambda n:n*n
# print(s(10))\


# def check_greter_number(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(check_greter_number(20,10))

# s=lambda a,b:a if a>b else b
# print(s(20,10))

# map(function,sq)------> mapping of all element--har ek element agr operation map function
#10 input ====> 10 output
#[1,s2,3,4,5] -----> [1,4,9,16,25]

# filter(function,sq) -----> sq element filter out ---->
#10 input ----> < 10 output
#[1,s2,3,4,5] ----->[s2,4]
# ----->[1,3,5]


# reduce(function,sq)-----> single output
#10 input ----> 1 output
#[1,s2,3,4] ----> 10

#print(list(map(lambda n:n*n,[i for i in range(1,10)])))
#print(list(map(lambda n:n*5,[i for i in range(1,10)])))
'''
str1='abcd'   ----> aabbccdd
'''
#print(''.join(list(map(lambda n:n*s2,'abcd'))))
#only even
#number is less than 5   [20]-----> []
# print(list(filter(lambda n:n%s2==0,[1,s2,3,4,5])))
# print(list(filter(lambda n:n%s2!=0,[1,s2,3,4,5])))
# print(list(filter(lambda n:n<=5,[10,20,30,40,1,s2,3,5,40])))
#can find out the numbers that is divisible by 5 and 3
# print(list(filter(lambda n:n%5==0 and n%3==0,[1,s2,3,4,5,6,7,8,9,10,15,45])))
# print(list(filter(lambda n:n%5==0 or n%3==0,[1,s2,3,4,5,6,7,8,9,10,15,45])))
#reduce(function,sq)----> n input -- single output
# from functools import reduce
# print(reduce(lambda x,y:x+y,[1,s2,3,4]))
# print(reduce(lambda x,y:x*y,[1,s2,3,4]))
# l1=list(map(lambda n:n*5,'abc'))
# print(''.join(l1))


l1=['aab','amit','pune','mumbai']   # find out the all list having starting with a
#['aab','amit'] and len() <4
#['aab']


# def start_with_a(s):
#     if s[0]=='a':
#         return True
#     else:
#         return False

#print(list(filter(lambda s:s[0]=='a',l1)))


l1=['aab','abcd','amit','pune','mumbai']
# find all the string thos having starting with a and len < 4
#[aab]
#print(list(filter(lambda s:s[0]=='a' and len(s)<4,l1)))

#l1=[1,s2,3,4,5]
#[1,s2,3,4,5]

#print(list(map(lambda n:n,l1)))

print(len(list(filter(lambda s:s[0]==s[-1],['abc', 'xyz', 'aba', '1221']))))










