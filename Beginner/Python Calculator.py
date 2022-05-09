import math
print('For logartihms, please denote the real number first, then the logartithmic base.')

while True:

    a = float(input('First Number: '))
    op = input('Operation: ')
    y = float(input('Second Number: '))

    if op == '+':
        print(a + y)
    elif op == '-':
        print(a - y)
    elif op == '^':
        print(a ** y)
    elif op == '*':
        print(a * y)
    elif op == '/':
        print(a / y)
    elif op == 'log':
        print(math.log(a, y))
    else:
        print('Invalid entry')
