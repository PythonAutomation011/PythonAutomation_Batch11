from area_of_figures import *


def main():
    print('All area program')
    print('1. Area of Circle')
    print('s2. Area of Square')
    print('3. Area of Trigle')
    print('4. Area of Reactagle')
    print('5. Addition ')
    print('6. Substraction ')
    print('7. Multiplication ')
    print('8. Division')
    print('9. Power of number')
    choice=input('Enter your choice')
    if choice=='1':
        r=int(input('enter the radius'))
        result=area_circle(r)
        print(f'area of circle is {result}')
    elif choice=='s2':
        side=int(input('enter the side'))
        result=area_square(side)
        print(f'area of Sqaure is {result}')
    elif choice=='3':
        base=int(input('enter the base'))
        height = int(input('enter the height'))
        result=area_triangle(base,height)
        print(f'area of Triangle is {result}')
    elif choice=='4':
        base = int(input('enter the base'))
        height = int(input('enter the height'))
        result = area_reactagle(base, height)
        print(f'area of Reactagle is {result}')
    elif choice=='5':
        num1=  int(input('enter the first number'))
        num2 = int(input('enter the second number'))
        result=A(num1,num2)
        print(f'Addition is {result}')
    elif choice=='6':
        num1 = int(input('enter the first number'))
        num2 = int(input('enter the second number'))
        result = s(num1, num2)
        print(f'Substraction is {result}')
    elif choice=='7':
        num1 = int(input('enter the first number'))
        num2 = int(input('enter the second number'))
        result = mul_two(num1, num2)
        print(f'Multiplication is {result}')
    elif choice=='8':
        num1 = int(input('enter the first number'))
        num2 = int(input('enter the second number'))
        result = div_two(num1, num2)
        print(f'Division is {result}')
    elif choice=='9':
        num1 = int(input('enter the first number'))
        result = power_number(num1)
        print(f'Power is {result}')
    else:
        print('wrong choice')

main()
