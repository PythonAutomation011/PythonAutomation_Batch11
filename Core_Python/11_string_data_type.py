#string ---is collection of sq in '' or "" or '''
#string is immutable in nature----->
#string is going use ----array
#positive----> 0 to len-1  negative ---> -1 to -len
#1 space as 1 char
#iterable in nature----> for loop, while loop


# s1= (10,20,30,40,50)
# #elenent and index position-----> enumarate()----> iterable(list,tuple,string)----> index position and element
#
# print(list(enumerate(s1)))  #position vaise consider karega
#operations of string---methods of string

'''
1 removing the space from the string
    1 strip()------> remove the space from both side(r and l)
    s2 rstrip() -----> remove the space from right side
    3 lstrip() -----> remove the space from left side
s2 finding the substring in string
    1 index() -----> will give the index position from the string
                if element is not present----> error
    s2 find() ----> will give the index position from the string
                if element is not present ----> no error ----> -1
    1 rindex()
    s2 rfind()

3 counting the substring----> count
    can you count the invi vowels in string
     a,u,e,i,o

4 replacement in string---->
    replace(oldstring,newstring)

5 split(seprator) -----> will divide the string based on seprator
                    -----> list convert
                    seprator----> space

    ''.join(list) ---list all element should be string


6 change the case in string
    1 upper()----> all the char in upper case(A to Z)
    s2 lower()----> all the char in lower case(a to z)
    3 swapcase() -----> upper-lower or lower-upper
    4 title() ----> all in title formate----> word 1st char ---capital
    5 capitalize() ----> first char

7 checking the all chars present in string
    1 isalnum() ----> True if all chars are aplhabets digit (a-z,A-Z,0-9)

    s2 isalpha() ----> True if all the chars are alphabets (a-z or A-Z)
    3 isdigit() ---> True if all the chars are digit (0-9)

    4 islower() -----> True if all the char string in lower
    5 isupper() ----> True if all the char string in upper
    6 isspace() ----> True if string having all the space
    7 istitle() ----> True if string title formate----> 1st char capital


#program to fetch special chars

can you fetch the numbers from the string and chars from the string


'''

str1='s12tep3upandl404earn'  #string intergers 12 3  404
l1=''.join([(i if i in '0123456789' else ' ') for i in str1])
l2=[int(i) for i in l1.split()]
print(l2)







import sys
sys.exit(0)
str1='0987654AAA'   #'12358'  'abcdefghk'
print(str1.isalnum())



import sys
sys.exit(0)
number_string=''
char_string=''
for i in str1:
    if i in '0123456789':
        number_string =number_string + i
    else:
        char_string = char_string + i
print(number_string)
print(char_string)












import sys
sys.exit()
for i in str1:
    if i.isdigit():
        number_string =number_string + i
    else:
        char_string = char_string + i
print(number_string)
print(char_string)




# for i in str1:
#     if i.isalpha():
#         char_string=char_string+i
#     else:
#         number_string=number_string+i
# print(char_string)
# print(number_string)



import sys
sys.exit(0)
#can print how many space in string
str1='python is programming laugauge'
l1=[]
for i in str1:
    if i.isspace():
        l1.append('0')
print(len(l1))
l3=[0 for i in str1 if i.isspace()]
print(len(l3))


import sys
sys.exit(0)

#can print all upper and lower chars

s1='pyThonMumbai'    #TM pyonumbai
upper_string=''
lower_string=''
for elemnt in s1:
    if elemnt.islower():
        lower_string=lower_string+elemnt
    else:
        upper_string=upper_string+elemnt
print(lower_string)
print(upper_string)






# s1='PYTHON is programming LANGUAGE'
# print(s1.capitalize())
#print(s1.title())  #Python Is Programming Language
# print(s1.upper()) #PYTHON IS PROGRAMMING LANGUAGE
# print(s1.lower()) #python is programming language
# print(s1.swapcase()) #python IS PROGRAMMING language