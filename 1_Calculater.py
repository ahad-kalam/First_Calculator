a = int(input('Enter your 1st value : '))
c = input('Enter your opreator like(+,-,*,/) : ')
b = int(input('Enter your 2nd value : '))

 
if c == '+':
    print(f'the sum of {a} and {b} is : {a + b}')
elif c == "-":
    print(f'the sub of {a} and {b} is : {a - b}')
elif c == "*":
    print(f'the multiplication of {a} and {b} is : {a * b}')
elif c == "**":
    print(f'the multiplication of {a} and {b} is : {a ** b}')
elif c == '/':      
    print(f'the divide of {a} and {b} is : {a/b}')
elif c == '//':
    print(f'the divide of {a} and {b} is : {a//b}')
elif c == "%":
    print(f'the reminder of {a} and {b} is : {a%b}')
else :
    print('invalib operator...!')


