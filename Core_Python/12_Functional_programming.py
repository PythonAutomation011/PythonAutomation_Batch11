'''
functions-------> block of code
            ----> we can reuse---code
        sytanx
            def function_name(arg1,arg2,arg3):
                statement
                statement
                stament
                print/return/yield
        calling
            function_name()
        return----> to take value of function and handover to the caller
                    always single
        if function is not returning nothing bydefault function will return None
        *** function 4 defferent way ****


        def f1(x,y):


        def f1():
            x=10
            y=20
            return x+y

        def f1(x,y):
            return x+y

        def f1():

modules in python ----> 2hr


1 taking something and returning nothing
s2 taking nothing and returning something
3
4

single in function but we can return multiple values, tuple

Type of arguments/ paramaters---> pass to the function

1 positional argument function
    import : position and number of parameters
s2 keyword argumenet function
    import: number of parameters
3 default arguement function
    3 formal arg ---->   <=3 actual
4 variable length argument
        *args ----> it always inside tuple
        function will return sum of all the parameter
        fun() --->0
        fun(1)---->1
        function(1,s2) ---3
        function(1,s2,3)---> 6
5 variable keyword argument function


#string ---> pallindrome or not
#square number
  5 ---25
  3---9
  6---36

 types of variables

 Global ----> define at module level----> variable is define outside the function
            we use inside the function----> access

            global keyword ----> global change


 Local -----> define inside the function-----> ref valide---funtion
            function execution is end----> ref use no

 Non local----> inner function----> closure property-----> inner function inside outer


nonlocal-----> compl---> outer variable hona chahiye
global====> no need


function alising-----> at run time we can change function name




Recursive Function----> a Calling itself----> inside we can call same function


fibonaciseries sum
reverse of string
sum of digits
power calculation
GCD
sum of all elements from list





pdb--->python debugger----> line by line

'''


import sys
sys.exit(0)
def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n-1, sum+n)

c = 999
print(recursive_function(c, 0))





import sys
sys.exit(0)
def create_list(l1):
    l2=[]
    for i in l1:
        if type(i)==list or type(i)==tuple or type(i)==str:
            l2.extend(create_list(i))
        else:
            l2.append(i)
    return l2
l1=[1,2,[3,4,(5,6),7],8,{1,2,3,4},'pune']  #[1,s2,3,4,5,6,7,8,1,s2,3,4]
print(create_list(l1))


import sys
sys.exit(0)
def sum_of_all_element(l1):
    sum1=0
    for i in l1:
        if type(i)==list:
            sum1=sum1+sum_of_all_element(i)
        else:
            sum1=sum1+i
    return sum1

l1=[1,2,[3,4,[5,6],7],8]  #1+s2+[3,4,[5,6],7],8
r=sum_of_all_element(l1)
print(r)









# sum1=0
# for i in l1:
#     sum1=sum1+i
# print(sum1)







#reverse the string---->recursive function












# str1='pune'
# output=''
# for i in str1:
#     output=i+output   #enup
# print(output)





# def reverse_string(s):   #AB       ''
#     if len(s)==0:
#         return s
#     return reverse_string(s[1:])+s[0]    #revser(B)+A    --->rever('')+BA
#
# r=reverse_string('AB')
# print(r)














import sys
sys.exit(0)
def sum_of_digit(n):    #5643       564      56       5
    if n==0:
        return 0
    return n%10+sum_of_digit(n//10)   #3 + sum_of_digit(564)    3+4+sum_of(56)   3+4+6+5

r=sum_of_digit(5643)
print(r)
















import sys
sys.exit(0)
def fibonaciseries(n):  #fact(s2)
    if n==0:      #s2==0    1==0
        return 0     #
    if n==1:      #s2==1    1==1
        return 1
    return fibonaciseries(n-1)+fibonaciseries(n-2)    #fibo(1)+ficbo(s2-s2)

result=fibonaciseries(7)
print(result)    #0,1,1,s2,3,5,8,13,21,34







import sys
sys.exit(0)

def fact(x):
    if x==0:
        result=1
    else:
        result=x*fact(x-1)   #5*4*fact(3)
    return result

r=fact(5)   #return-----> value bahar ayega----> caller
print(r)













import sys
sys.exit(0)
def f1():
    x=10
    y=20
    print(x,y)

f1()

f1()



import sys
sys.exit(0)



def check_number(n):
    if n in [1,2,3,4,5,6,7,0]:
        print('hi')
    else:
        print('no')

s=check_number       #a=10   b=a    ---->
print(id(s),id(check_number))
print(type(s))




import sys
sys.exit(0)
def outer():
    #x=1000
    #print(f'x value at 89 line :{x}')  #1000
    def inner():
        global x
        x=200
        print(f'x value at 93 line:{x}')   #200
    #print(f'x value at 94 line: {x}')  #1000
    inner()
    print(f'x value at 96 line:{x}')   #200

outer()






































import sys

sys.exit(0)
def outer():
    x=100
    print(x)
    def inner():
        nonlocal x
        x=200
        print(x)
    print(x)
    inner()
    print(x)
outer()




import sys

sys.exit(0)
x='city'
y=20
z,v,s=10,'mumbai',30

def f1():
    print(x,y,z,v,s)

def f2():
    global x
    x='contry'
    global y
    y='pune'
    print(x, y, z, v, s)

print(x,y,z,v,s)
f1()
f2()
print(x,y,z,v,s)







import sys
sys.exit(0)
def f1():
    x=10    #local variable to f1
    print(x)
def f2():
    global x
    x=100   #local to f2
    print(x)
def f3():
    print(x)
def f4():
    print(x)

f2()  #100
print(f'x value before calling function {x}')  #100 why ??
f1()  #10
f3()  #100
f4()   #100
print(f'x value after calling function {x}')  #100




import sys
sys.exit(0)
def f1():
    global var1   # going the change the global variable
    var1=200   #local variable
    print(var1)

f1()
print(var1)













# def print_data(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# print_data(v=10,z=20,s=30,r=40) #dict----> keys


import sys
sys.exit(0)
def sum_of_elemenet(*a):
    sum1=0
    for i in a:
        sum1=sum1+i
    return sum1

r1=sum_of_elemenet(1,2,3,4,5,6,7,8,9,10)
print(r1)







import sys
sys.exit(0)
def chec_pallindrom(str1):
    if str1==str1[::-1]:
        return True,'yes'
    else:
        return False,'No'







import sys
sys.exit()
def sample():
                                a=10
                                b=20
                                print(a+b)
                                print(a-b)
                                print(a*b)
                                print(a/b)

sample()   #outside
print('hello hi')
sample()






# def print_vaibhav():
#     print('hello vaibhav')
#
# print(10)

# print_vaibhav()


import sys
sys.exit(0)
def print_10_hello():
    for i in range(10):
        print('hello')


print_10_hello()
print('hi this is vaibhav')
print_10_hello()
print('this is pune city')
print_10_hello()