#Dict------>Mutable------> collection of key and values ---> items in dict
#dict collection immutable and mutable object
#hashtable principal on keys
#there is no array concept----> index no----> slice no
#dict is order dict based on keys-----> but order dict----> only after python 3.6

#key -----> immutable nature
        #int,floa,com,None,True,False,string,tuple
        #unique in nature

        #single True,False,None

#value----> immutable or mutable ----> all
    #unique or duplicates
'''
python s2
d1={1:10,s2:200,'city':'pune','a':'aa',3:300}
print(d1)
output---->
{'a': 'aa', 1: 10, s2: 200, 3: 300, 'city': 'pune'}


CRUD in Dict
create
    d1={} or d1=dict()
Adding the element inside dict:
    dict[key]=value
Read from dict
    d1[key] ----> value -----> keyerror if key is not present
    d1.get(key)---> value ----> no error
    d1.get(key,defaulval) ----> if key present it will return value else it will return default value
    for loop
    keys() ----> all the keys of dict
    values() ----> all the values of dict
    items() ----> all the items of dict---tuple
Update
    d1[key]=value      -----> always update the dict
    d1.setdefault(key,value) ---> if key is present no need to update
                                else it will update the dict
    d1={}
    d2={}
    d1.update(d2) -----> update d1 with d2
Delete
    pop(key) ----> delete the key and value based on key
    popitem() ----> random item will delete
    clear()  -----> it will make dict as empty
    del d[key]
    del d1
    dict.fromkeys([1,s2,3,4],None)

booking tickets
5 tickets --->[101,202,1001,303,444,505]

single line list,set,dict ???----comprehession in python
string data----->


string----after string fundamental---->

 online

 candiate 1 ----->






'''


# import sys
# sys.exit(0)
# class_python=[1,s2,3,4,5,6,7,8,9,10]
# d1=dict.fromkeys(class_python,None)
# d1[1]='akshay'
# d1[s2]='sakshi'
# d1[3]='mayur'
# d1[4]='prashant'
# d1[5]='aaa'
# d1[6]='xyz'
# d1[7]='ram'
# d1[8]='sham'
# d1[11]='vyz'
# print(d1)





#can you convert this dict to new formate----> replay the key with value and value with key
d1={1:10,2:20,3:30,4:40,5:500,7:400}
print(d1)
d2={}

for k,v in d1.items():
    d2[v]=k

print(d2)










import sys

sys.exit(0)
#can you create the dict of 0 to 10
#key will be number and value will be squeare of thata
# if number is even then you give the square , odd the cube
d1={}
for i in range(0,11):
    if i%2==0:
        d1[i]=i*i
    else:
        d1[i]=i*i*i
print(d1)
