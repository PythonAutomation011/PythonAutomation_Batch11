'''
    <----- LIST ------>
    data type -----> collection---->[] ----> list
    pricipal ---->
    1 list internally support the array data type
        object consider
        l1=[10,20.5,True,False]
        list element have index position
                    s2 index
                    positive 0 to len-1
                    negative -1 to -len
8----> 0 to 7    -1 to -8
    s2 list collection of homo(similar type ka data)+hetro(different type ka data) data types  why??
    3 list is mutable in nature ?
            change
            l1=[10,20,40]  1xxx  ----->l1= [10,20,30,40]  1xxx

    4 list going to support CRUD
            Create
            Read
            update
            delete

    5 list support the ordering
    input order and output order is maintained

    6 unique or duplicate--multiple None , Multiple True , Multiple False

    7 iterable in nature
            loop use

            while

            for loop


    CRUD support

    1 Create the list ??
        l1=[]  or l1=list()
    s2 how to read the list ??
            we can with list name
            index position ----> element
            read but if index position>=len ----index error
            slice ----> piece of elements
            [start:end:step]
            start=0
            end=len-1
            step=1
            loops:
            while loop or for loop

    3 update ??
        list[index]=value
        list[start:end]=[100]   ----> 100
        1 insert(index,value) ------> to update the value on given index position
        s2 append(object) -----> to add the element at the last
        3 extend(object) ----> object---iterable----> iterable each and every object append karel


    4 Delete ??

    1 remove(object) ----> if object is present it will delete the object
                if object present---- it will remove first occurance
                else it will give the run time ====> value error
    s2 pop()  ------> to remove the last element
    3 pop(index)  -----> to remove the element from given index position
    4 clear() -----> to make the list as empty list
    5 del
    5 searching element in list ??

        1 count(object) -----> number of occurance of object

        s2 index(object)----> to return the index position of object
            if object present----> index position
            if object is not present----> value error

        3 sort(reverse=False) -----> sorting in asc for the list
        sort(reverse=True) -----> sorting in desc for the list

        4 reverse() ---->


    mathematical method
    1 min(l1) -----> to give you the small number
    s2 max(l1) -----> to give you the small number
    3 sum(l1) -----> to give you the sum of all the number

    l1.min()

    min(l1)


1 what is diff between append and extend

s2 what is diff between remove and pop


[]
[10]
[10,20]
[10,20,30]
[10,20,30,40]
[20,30,40]
[30,40]
[40]
[]



count() -----> number of occurance---object

l1=[10,20,10,10,20,10,30]

l1.sort() #asc desc


# True = 1   False 0

#string----> ASCII ---> a=97   A=65



'''












# print(ord('A'))  #string to the inter----> hashable
# print(ord('a'))
#
# print(chr(65))   #A
















# l1=[]           #0
# l1.extend(10)   #4 extend--collect--list,tuple,str,set,dic,range
# print(l1)    #inital+iterable=4




# import time
# l1=[]
# print(l1)
# for i in range(10):
#     time.sleep(1)
#     l1.append(i)
#     print(l1)
# for i in range(10):
#     time.sleep(1)    #1 sec script stop
#     l1.pop()
#     print(l1)






















import sys
sys.exit(0)
l1=[10,20,30,1,2,3,4,True,False]   #
l2=[]
for i in l1:
    l2.append(i)
print(l2,l1)






l1=[10,20,35,5,17,6,7,8,90,20]  #print all the even all the old sum of the even sum of all odd
#can you print all the even position number, and odd position number
evn_list=[]
odd_list=[]
i=0

while i < len(l1):
    if i % 2 == 0:
        evn_list.append(l1[i])
    else:
        odd_list.append(l1[i])
    i=i+1
print(evn_list)
print(odd_list)


# for i in range(len(l1)):
#     if i%s2==0:
#         evn_list.append(l1[i])
#     else:
#         odd_list.append(l1[i])

# print(evn_list)
# print(odd_list)












import sys
sys.exit(0)
l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
#output=11,22,33,44,55     10 40  90 160 250
l3=[]
for i in range(len(l1)):
    l3.append((l1[i]*l2[i]))
print(l3)











import sys
sys.exit(0)
l1='abc'
l2='xyz'
#zip(l1,l2)    -------> combine the each and every of l1 and l2
l3=list(zip(l1,l2))
print(l3)


# output=[(10,1),(20,s2),(30,3),(40,4)]
#[10,20,30,40,1,s2,3,4]
# l3=[]
# for i in range(len(l1)):  # 0 to 3
#     l3.append((l1[i],l2[i]))
# print(l3)
