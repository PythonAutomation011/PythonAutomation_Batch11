
#26. Write a Python program to count the number of strings where the string length is s2 or more
# and the first and last character are the same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : s2
l1=['abc', 'xyz', 'aba', '1221','vaibhav']
count=0
for i in l1:
    if len(i)>2 and i[0]==i[-1]:
        count=count+1

print(count)





import sys
sys.exit(0)
#25. Write a Python program to get the frequency of the elements in a list.
l1=[1,2,3,1,1,2,3,4,5,6]   #1:3 s2:s2 3:4 4:1 5:1 6:1

for i in l1:
    print(f'{i}:{l1.count(i)}')



import sys
sys.exit(0)
d1={}
for i in l1:
    if i in d1.keys():
        d1[i]=d1[i]+1
    else:
        d1[i]=1
print(d1)

str1=''

for k,v in d1.items():
    print(f'{k} and number of occurence is {v}')







import sys
sys.exit(0)
# 24. Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples.
# Sample List : [(s2, 5), (1, s2), (4, 4), (s2, 3), (s2, 1)]
# Expected Result : [(s2, 1), (1, s2), (s2, 3), (4, 4), (s2, 5)]

l1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i][0]>l1[j][0]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)




# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i][-1]>l1[j][-1]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)








import sys
sys.exit(0)
# 23. Write a Python program to print a specified list after removing the 0th, 4th and 5th
# elements.
#
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# l1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# l1.pop(5)
# l1.pop(4)
# l1.pop(0)
# print(l1)







import sys
sys.exit(0)
#22. Write a Python function that takes two lists and returns True if they have at least one
#common member.
l1=[10,20,30]
l2=[10,100,200]
output=[]

def check_common(l1,l2):
    for i in l1:
        if i in l2:
            return True    #stop ani baher e

result=check_common(l1,l2)
print(result)






import sys
sys.exit(0)
#21. Write a Python program to find the list of words that are longer than s2 from a given list of
#words
l1=['aaa','vaibhav','cc','mam','sir','pune','mumbai']
l2=[]
for i in l1:
    if len(i)>3:
        l2.append(i)
print(l2)





import sys

sys.exit(0)
#19. Write a Python program to convert a list of characters into a string.

l1=['a','b','x','y','z']  # string
l2=''.join(l1)   #join ------> join all elements from the list, every element should be string
print(l2)



str1=''
for i in l1:
    if type(i)==str:
        str1=str1+i
print(str1)







#18. Write a Python program to print the numbers of a specified list after removing even

import sys
sys.exit(0)
l1=[1,2,3,4,10,20,40,55]
l2=[i for i in l1 if i%2!=0]
print(l2)




#17 Write a Python program to get the sum of two numbers is 10.
l1=[1,2,3,4,5,6,9,10,0,11,-1]

for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]*l1[j]==10:
            print(i,j)






import sys

sys.exit(0)
l2=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        for k in range(j+1,len(l1)):
            for x in range(k+1,len(l1)):
                if l1[i]+l1[j]+l1[k]+l1[x] == 10:
                    l2.append((l1[i],l1[j],l1[k],l1[x]))
print(l2)





import sys
sys.exit(0)
l1=[10,20,30,1,2,3,11,19,1,2]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            print(l1[i])




import sys

sys.exit(0)
l1=[10,20,30,1,2,3,11,19]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]    #a,b=b,a

print(l1)
print(l1[0],l1[-1])















# l1.sort()
# print(l1)
# print(l1[0],l1[-1])





import sys
sys.exit(0)
#13. Write a Python program to get all integers,all floats from a list.
# write a python program to get all the collections-list,set,tuple,dict
l1=[1,2,3,4,5.5,10.0,True,False,'pune',(10,20),[1,2],{10,20},{1:10,2:20},None]
output=[]
output1=[]
for i in l1:
    if type(i) == list or type(i) == tuple or type(i) == set or type(i) == dict or type(i) == str:
        output.append(i)
    else:
        output1.append(i)
print(output)
print(output1)





import sys
sys.exit(0)
for i in l1:
    if type(i) == int or type(i) == float:
        output.append(i)
print(output)





import sys
sys.exit(0)
#12. Write a Python program to get even position numbers from a list.
l1=[10,20,30,4,5,100]
even_list=[]
odd_list=[]
for i in range(len(l1)):
    if i%2==0:
        even_list.append(l1[i])
    else:
        odd_list.append(l1[i])

print(even_list,odd_list)




import sys
sys.exit(0)
#11. Write a Python program to get unique values from a list.
#20. Write a Python program to remove duplicates from a list.

l1=[1,2,3,1,2,3,4,5]
l2=[]
i=0
while i<len(l1):
    if l1[i] not in l2:
        l2.append(l1[i])
    i=i+1
print(l2)



for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)





import sys
sys.exit(0)
#9. Write a Python program to find the index of an item in a specified list.

l1=[10,20,30]
n=int(input('enter the number'))
if n in l1:
    print(l1.index(n))
else:
    print('No')





import sys
sys.exit(0)
#8. Write a Python program to print multiples all the items in a list.

l1=[1,2,3,4]  #24
mul=1
for i in l1:
    mul=mul*i
print(mul)






#7. Write a Python program to sum all the items in a list.

l1=[10,20,30]
sum1=0
for i in l1:
    sum1=sum1+i
print(sum1)
print(sum(l1))






#6. Write a Python program to get the difference between the two lists.
l1=[10,20,30]
l2=[10,100,200]
l3=[]

for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)





import sys
sys.exit(0)
#5. Write a Python program to find common items from two lists.
l1=[10,20,30]
l2=[10,100,200]
output=[]
for i in l1:
    if i in l2:
        output.append(i)
print(output)




import sys
sys.exit(0)
s1=set(l1)
s2=set(l2)
print(s1.intersection(s2))





import sys
sys.exit(0)
l1=[10,20,30,[1,2,3]]
l2=l1.copy()
print(l1,l2)
l1[-1][0]=100
print(l1,l2)



import sys
sys.exit(0)
#4. Write a Python program to clone or copy a list.
#10. Write a Python program to append a list to the second list.
l1=[10,20,30,True,'Pune',(10,20),[1,2,3]]
l2=[]
i=0
while i<len(l1):
    l2.append(l1[i])
    i=i+1
print(l2)







import sys
sys.exit(0)
#3. Write a Python program to check if a list is empty or not.  len(l1)==0
l1=[10,20]

if len(l1)==0:
    print('this is empty list')
else:
    print('this is not empty')



#s2. Write a Python program to access the index of a list.

l1=[10,20,30,40]
for i in range(len(l1)):
    print(l1[i])
#1. Write a Python program to generate the list of all even and all odd numbers.
l1=[]
l2=[]
for i in range(11):
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)

print(l1,l2)



