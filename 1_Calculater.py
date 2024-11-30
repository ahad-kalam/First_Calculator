num1 = int(input('Enter your 1st value : '))
c = input('Enter your opreator like(+,-,*,/) : ')
b = int(input('Enter your 2nd value : '))

 
if c == '+':
    print(f'the sum of {num1} and {b} is : {num1 + b}')
elif c == "-":
    print(f'the sub of {num1} and {b} is : {num1 - b}')
elif c == "*":
    print(f'the multiplication of {num1} and {b} is : {num1 * b}')
elif c == "**":
    print(f'the multiplication of {num1} and {b} is : {num1 ** b}')
elif c == '/':      
    print(f'the divide of {num1} and {b} is : {num1/b}')
elif c == '//':
    print(f'the divide of {num1} and {b} is : {num1//b}')
elif c == "%":
    print(f'the reminder of {num1} and {b} is : {num1%b}')
else :
    print('invalib operator...!')


