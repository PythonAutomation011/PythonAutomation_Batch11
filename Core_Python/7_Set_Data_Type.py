#set -----> collection of objects
#mutable in nature----> CRUD
#objects------> immutable, we cant use mutable objects inside the set
#hashtable----> array, list
#set----> collection of all unique values
#set going to remove the duplication
#unorder data type
#there no index position----> slice---> No
#iterable in nature-----> loop concept
#can i use set inside set ??? No
#method ---CRUD
#create
#s1={1,s2,3,4} # with help of {,,}
#set()
#{}-----> dict data type consider
#read----> loop ---->
#update  ---- > s2
#add(object)----> add element in side the set ----> No ---why--->
#{1,s2,3,'pune'}
#update(object)---> object should be iterable
#{1,s2,3,p,n,u,e}
#Deletion
#clear() ----> delete all the object from the set and return empty set
#del set -----> delete the set object from memory
#pop() ------> remove the random element from the set---> arbitory element
#remove(object)----if object present ---> remove the object else error
#discard(object)---> if object present---> remove the object else Nothing
#pop---->

'''
    data
    duplicate, order,3day data ----> list

    duplicate,order ------> tuple

    unique,no order, 3day data ----> set





Set Operations-----> multiple set operation

1 union ----> all the elements from both set

s1 ={1,s2,3,4,10}
s2={1,s2,100,200}
---->{1,s2,3,4,10,100,200}

union or |


s2 intersection ----> common elements from both set
s1 ={1,s2,3,4,10}
s2={1,s2,100,200}
-------> {1,s2}

interesection or &


3 difference ----->
s1 ={1,s2,3,4,10}
s2={1,s2,100,200}

s1-s2

s2-s1


4 symmetric difference

s1 - s2 union s2-s1

check in set

1 issubset--->
s1={1,s2,3}
s2={1,s2}
s2 issuperset---->
3 isdisjoin---->
size set>size list > size tuple

'''
#can you find out duplicates from the list
from collections import Counter   # Counter(iterable) ----> return number occurance of each object

l1= {10,20,10,10,20,30}  #iterate and jiscount s2 print  ----> number occurance = s2
print(Counter(l1))

# d1={}
# for i in l1:
#     if i in d1:
#         d1[i]=d1[i]+1
#     else:
#         d1[i]=1


# for k,v in d1.items():
#     if v==s2:
#         print(k)








# s1=set()
# for i in l1:
#     if l1.count(i)==s2:
#         s1.add(i)
# print(s1)



# set_1=set()
# set_2=set()
# for i in l1:
#     if i in set_1:
#         set_2.add(i)
#     else:
#         set_1.add(i)
# print(set_2)









# s1='vaibhav'
# print(set(s1))



import sys
sys.exit(0)
l1=[10,20,30,100,200,1,2,3]
l2=[1,2,3,100]
l3=[]

print(list(set(l1)-set(l2)))


# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l3)




import sys

sys.exit(0)
s1={1,2,3,4,5}  #memory
l1=[1,2,3,4,5]  #memory
t1=(1,2,3,4,5)  # memory tuple
print('list',sys.getsizeof(l1))
print('tuple',sys.getsizeof(t1))
print('set',sys.getsizeof(s1))





import sys
sys.exit(0)
#missing numbers in l2
l1=[10,20,30,100,200,1,2,3]
l2=[1,2,3,100]
l3=[]

print(set(l1)-set(l2))  #set ----> hashtable-----> index position       shifting


s1={1,2,3}
l1=[1,2,3]

#50%8 -----> s2 ----> 2nd bucket -----> 1
#50----->1+1+1+1     -----> 4 iteration

# s2 from set and from list

#s2%8 ----> 1st -----> memory address----1

# [1,3]   ---      s2 iteration










import sys
sys.exit(0)
#volwels in string
str1='pune is a city in maharastra'  #
s1={'a','i','e','o','u','A','I','E','O','U'}
s2=set(str1)
print(s1.intersection(s2))




# s2=set()
# for i in str1:
#     s2.add(i)
# print(s2)






import sys
sys.exit(0)

s1={1,2,100,200,10}
s2={30,100,200,'pune'}
print('union',s1.union(s2)) #{1, s2, 100, 200, 10, 'pune', 30}
print('intersection',s1.intersection(s2)) #{100,200}
print('s1-s2',s1.difference(s2)) #{1,s2,10}
print('s2-s1',s2.difference(s1)) #{'pune', 30}
print('sym_diff',s1.symmetric_difference(s2)) #{1,s2,10,pune,30}