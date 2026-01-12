'''

Comprehension----> pythonic way to deal with data types in single line


for loop--->

list comprehession

set comprehession

dict comprehession



can you create the list of all numbers from 0 to 10
can you create a set of all numbers from 0 to 10
can you create the dict of all number, key number and value number*number

1 for loop
    for i in range(1,11):
        statement

 l1=[i for i in range(1,11)]
 s1={i for i in range(1,11)]
 d1={i:i*i for i in range(1,11)}


can you create the list of all numbers from 0 to 10 if number is even
can you create a set of all numbers from 0 to 10 if number is even
can you create the dict of all number, key number and value number*number if number number

for loop:
    if
s2 for loop with if condition
    l1=[i for i in range(1,11) if condition]
    s1={i for i in range(1,11) if condition}
    d1={i:i*i for i in range(1,11) if condition}

3 for loop with if condtion else part
can you create the list of all numbers from 0 to 10 if number is even square else cube of that number
can you create a set of all numbers from 0 to 10 if number is even square else cube of that
can you create the dict of all number, key number and value number*number if number number else cube value


give the list of all the sq number if number is even else cube if number>5


for outer:
    for inner

#[statement for outer for inner]

list,set,dict

tuple comprehession---not supported-----> it will return generator object


MultiDimential List----->
[[],[],[],[]]


hotel --- 5 rooms ----> 7 days


l1=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


3rooms and 3days---> input user


company----->[eno,ename,eadd]  3 employee
[[101,'aaa','pune'],[202,'xyz','mumbai'],[304,'aaa','banglore']]
'''
nemp=3
details=['eno','ename','eadd']

# x=[[input(f'enter the detail: {d}') for d in details] for i in range(1,nemp+1)]
# print(x)

a='ram'

print(f'name is {a}')




# l1=[[int(input('enter the day')) for j in range(s2)] for i in range(3)]
# print(l1)



# nrooms=5
# ndays=7
#
# l1=[[0 for j in range(ndays)] for i in range(nrooms)]
# print(l1)




import sys
sys.exit(0)
t1=[i for i in range(1000000)]
print(t1.__sizeof__())

t1=(i for i in range(1000000))
print(t1.__sizeof__())



l1=[]
for i in range(3):
    for j in range(2):
        l1.append((i,j))

print(l1)
l3=[(i,j) for i in range(3) for j in range(2)]
print(l3)



import sys
sys.exit()

print([i for i in ['abc', 'xyz', 'aba', '1221'] if i[0]==i[-1] and len(i)>2])

for i in range(10):
    print(i)

for i in range(10):
    print(i)





# l1=[i*i if i%s2==0 else i*i*i for i in range(10) if i>s2]
# print(l1)

# l1=['aa','apple','mango','pune']
# l3=[i for i in l1 if len(i)>4]
# print(l3)

# l1=[10,20,30]
# l2=[10]
#
# l3=[i for i in l1 if i in l2]
# print(l3)

# d1={}
# for i in range(11):
#     if i%s2==0:
#         d1[i]=i*i
#     else:
#         d1[i]=i*i*i
# print(d1)
#
# d2={i:(i*i if i%s2==0 else i*i*i) for i in range(11)}
# print(d2)
















# s=set()
#
# for i in range(11):
#     if i%s2==0:
#         s.add(i*i)
#     else:
#         s.add(i*i*i)
# print(s)
#
# s2={i*i if i%s2==0 else i*i*i for i in range(11)}
# print(s2)











# l1=[]
# for i in range(11):
#     if i%s2==0:
#         l1.append(i*i)
#     else:
#         l1.append(i*i*i)
# print(l1)
#
# l2=[i*i if i%s2==0 else i*i*i for i in range(11)]
# print(l2)








import sys
sys.exit(0)
d1={}

for i in range(10):
    if i%2==0:
        d1[i]=i*i
print(d1)

d2={i:i*i for i in range(10) if i%2==0}
print(d2)



# s1=set()
#
# for i in range(10):
#     if i % s2 == 0:
#         s1.add(i)
# print(s1)
#
# s2={i for i in range(10) if i%s2==0}
# print(s2)



# l1=[]
# for i in range(10):
#     if i%s2==0:
#         l1.append(i)
# print(l1)
#
# l1=[i for i in range(10) if i%s2==0]
# print(l1)

import sys
sys.exit(0)





s1=set()
for i in range(10):
    if i%2==0:
        s1.add(i)
print(s1)

d1={}
for i in range(10):
    if i%2==0:
        d1[i]=i*i
print(d1)






import sys

sys.exit(0)




# l1=[]
# for i in range(11):
#     l1.append(i)
# print(l1)

# l1=[i for i in range(11)]
# print(l1)


# s1=set()
# for i in range(11):
#     s1.add(i)
# print(s1)
#

# s1={i for i in range(11)}
# print(s1)

# d1={}
# for i in range(11):
#     d1[i]=i*i
# print(d1)

# d1={i:i*i for i in range(11)}
# print(d1)


#0 to 5 square

l1=[]
for i in range(0,6):
    l1.append(i*i)
print(l1)

l2=[i*i for i in range(0,6)]
print(l2)