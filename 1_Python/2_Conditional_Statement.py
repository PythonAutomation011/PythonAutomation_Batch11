'''
    conditional statement----->
            condition based on operator-----> True or False
statement1
statement2
statement3
banana <20rs
apple  ==5
orage
ghar
    1 if condition:
        statement1
        statement2
        statement3
      statmenet4
    eg -: check of temp is high
    sys---system
    sys.exit(0)----> baher leke ayenge

    2 if condition:
        statement1
    else
        statement2

    statement1 if conditon else statement2

    3
    if condition:
        statement1
    elif condition:
        statement2
    elif condition:
        statement3
    else :
        statement4


 marks> 90 ----> engineer
 marks>80 ----> dr
 marks>70 ----> layer
 marks>60 ----> actor

 95 ---->


Iterative statement-----> Saturday 2hr

for


while

Sunday------> setup of course   - 3/4 hr-----> 2 session on sunday
        Linux commands in Automation/QA
        GITHUB
        GENAI in Coding part



Data types ----->

list data 2

tuple 1

set 2

dict 2

string 2











'''
import sys

print('enter the your choice : 1-Add, 2-Sub, 3-Multi, 4-Div, 5-Floor')
choice = int(input())
x=int(input('enter the first number : '))
y=int(input('enter the second number : '))

if choice == 1:
    print(x+y)
elif choice == 2:
    print(x-y)
elif choice == 3:
    print(x**y)
elif choice == 4:
    print(x/y)
elif choice == 5:
    print(x//y)
else:
    print('stop you enter wrong choice')

#traffic signal ----> Yellow--get ready , Red --stop  , GO\
# signal="white"
#
#
# if signal=="Yellow":
#     print("get ready")
# elif signal=="Red":
#     print("stop")
# else:
#     print("go")













# marks=95
# if marks>80:
#     print('dr')
# elif marks>90:
#     print('engineer')
# elif marks>70:
#     print('layer')
# elif marks>60:
#     print('actor')
# else:
#     print('MLA')









# #marks----> 35 Pass else failed
# marks=int(input('enter the marks'))
# result='pass' if marks>35 else 'fail'   #shorthand technical
# print(result)





#facebook page----> admin123,admin12----> corrent----> login else failed to login

# username=input('enter the username')
# password=input('enter the password')
# if username=='admin123' and password=='admin12':
#     print('login success')
# else:
#     print('login failed')

# result='login success' if username=='admin123' and password=='admin12' else 'login failed'    #73 chars---PEP8
# print(result)





sys.exit(0)
#check given number is even or odd
n=int(input('enter the number'))

result='even' if n%2==0 else 'odd'
print(result)
print('thank you bye bye')







# if n%2==0:
#     print('even')
# else:
#     print('odd')












# if condition:
#     statement1
#     statement2
#     statement3
# else:
#     statement4
#     statement5
#
# statement6








sys.exit(0)
#person----> 10AM ---breakfast
#person ----> 1pm ----> luanch
#person----8pm-----dinner




sys.exit(0)
#user going to enter the number
#if number%2==0 then print even
#if number%5==0 then print divisible by 5
#if number%3==0 then print divisible by 3


n=60
if n%2==0:
    print('number is even')
if n%5==0:
    print('number is divisible by 5')
if n%3==0:
    print('number is divisible by 3')







sys.exit(0)
#check given is even-----> number%2==0

n=int(input('enter the number'))
if n%2==0:
    print('even')

print('finised')
print('bye bye')







sys.exit(0)
#check if user is adult
#age>18

age=int(input('enter you age'))
if age>18:
    print('you are younger')









sys.exit(0)


temperature=90

if temperature>99:   #90>99 ---False
    print("temperature is high")

print('bye')
print('welcome to home')
