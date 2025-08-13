

'''
for element in iterable:

    print(element)

1 for string

2 for list

3 for tuple

4 no set and dict

for i in set1



for i in dict1 ---->***  item


1 can print the all even numbers from 1-25
for i in range(0,25,2):
    print(i)



2 can print the all the odd numbers from 1-25
for i in range(1,25,2):
    print(i)

for i in range(0,25):
    if i % 2 == 1:
        print(i,end=' ')  #end next line with previous line


3 can print sum of all the even numbers from 1-10
4 can print sum of all the odd numbers from 1-10
5 can print mul of all the even numbers from 1-10
6 can print mul of all the odd numbers from 1-10


[1,2,3,4,5,6,7,8,9,10...25]


nested for ---for loop for loop
'''
# for i in range(0,3):
#     print('A')   #0 1 2
#     for j in range(0,2):  #0 1
#         print('B')

l1=[1,2,3,4,5,6,9,10,-1,12,-2,9]   # 2 numbers that having sum 10
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        for k in range(j+1,len(l1)):
            for l in range(k+1,len(l1)):
                for m in range(l+1,len(l1)):
                    if l1[i]+l1[j]+l1[k]+l1[l]+l1[m]==10:
                            print(l1[i],l1[j],l1[k],l1[l],l1[m])




















# l2=[i for i in [1,2,3,4,5,10,20,30,40] if i%5==0 or i%3==0]
#
# print(l2)

# i=0
# while i<len(l1):
#     if l1[i] % 3 == 0 or l1[i] % 5 == 0:
#         print(l1[i])
#     i=i+1




# for i in l1:
#     if i%5==0 or i%3==0:
#         print(i)











import sys
sys.exit(0)

l1=['aaa','abc','def','ghi','amit','akshay']
for i in l1:
    if i[0]=='a' or i[0]=='g':
        print(i)







#volwels  aeiou
# str1='pune vaibhav stepup learn'   #u e a i a e u e a count of volwels
# vol='aeiou'
# count=0
# # for i in str1:
# #     if i in vol:
# #         print(i)
#
# l1=[i for i in str1 if i in vol]
# print(l1)

# i=0
# while i<len(str1):
#     if str1[i] in vol:
#         print(str1[i])
#         count = count + 1
#     i = i + 1
# print(count)

import sys
sys.exit(0)
sum1=0
str1='pu1ne i2s cit4y in ma5ha6rastra9'
for i in str1:
    if i in '0123456789':
        sum1=sum1+int(i)  #1+2+4+5+6+9
print(sum1)

sum1=1
str1='pu1ne i2s cit4y in ma5ha6rastra9'
for i in str1:
    if i in '0123456789':
        sum1=sum1*int(i)  #1+2+4+5+6+9
print(sum1)

# i=0
# while i<len(str1):
#     if str1[i] in '0123456789':
#         print(str1[i],end=' ')
#     i=i+1








import sys
sys.exit(0)
even_mul=1
odd_mul=1
i=1

while i<6:
    if i % 2 == 0:
        even_mul =even_mul*i
    else:
        odd_mul =odd_mul*i
    i=i+1

print(even_mul,odd_mul)






even_Sum=0
odd_Sum=0

for i in range (0,11):
    if i % 2 == 0:
        even_Sum =even_Sum+i
    else:
        odd_Sum =odd_Sum+i

print(even_Sum)
print(odd_Sum)



