
#range()   python 3.x ---iterable
#total 3 different
#1 range(n) -----> 0 to n-1
#2 range(start,n) -----> start to n-1
#3 range(start,end,step) -----> step skip the element ---step=2 skip 1 element

# str1='pune'
#
# for i in range(len(str1)):
#     print(str1[i],i,i-len(str1))

str1='pune is the city in maharashtra'
for i in range(0,len(str1),2):
    print(str1[i])


#for loop----> string,list,tuple,set,dict, range

#for i in iterable:
#   print(i)

# l1=["10",20,30,40,1.5,'pune']
# for i in l1:
#     if type(i)==str:
#         print(i)


#QUESTION-----> CAN YOU PRINT ALL THE INT FROM LIST

import sys
sys.exit(0)
# 324

num=124
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

print(rev)


import sys
sys.exit(0)
#3 ----> fact
#2 ----fact
#5----> fact

n=4
fact=1

while n>0:
    fact=fact*n
    n=n-1

print(fact)




import sys
sys.exit(0)
#1 to 5 you need to calcuate the product of all element
#1*2*3*4*5


i=1
mul=1   #
while i<=5:
    mul=mul*i
    i=i+1
print(mul)

import sys
sys.exit(0)
#sum of all the numbers from 1 to 10
#1,2,3,4,5,6,7,8,9,10 ----->

i=1
total=0
while i<=5:
    total=total+i
    i=i+1
print(total)

import sys
sys.exit(0)
# 7 -----> want to generate the table for 7
#7 14 21 28 35-------70
num=int(input('enter the number'))
i=1
while i<=10:
    print(num*i-1)
    i=i+1
  
import sys
sys.exit(0)
s1='pune'   #len-1      i<len
x=0
while x<len(s1):
    print(s1[x],x,x-len(s1))   #s1[0]    s1[1]    s1[2]   s1[3]
    x=x+1

import sys
sys.exit(0)
print(s1[0])
print(s1[1])
print(s1[2])
print(s1[3])


import sys
sys.exit(0)
i=0    #init
while i<6:    #condition
    print(i)
    i=i+1     #increment

