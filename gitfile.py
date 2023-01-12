def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print('1.Addition\n2.Substraction\n3.Multiplication\n4.Division')
while True:
    choice = int(input('Enter the choice:'))
    if choice in (1, 2, 3, 4):
        try:
            x = float(input('Enter the first number:'))
            y = float(input('Enter the second number:'))
        except ValueError as msg:
            print('Invalid Input',msg)

        if choice==1:
            print(f"Addition of {x} and {y} is:",add(x,y))
        elif choice==2:
            print(f"Substraction of {x} and {y} is:", sub(x,y))
        elif choice==3:
            print(f"Multiplication of {x} and {y} is:", mul(x,y))
        elif choice==4:
            print(f"Division of {x} and {y} is:", div(x,y))
        check = input('Do you want to continue :[yes/no]')
        if check=='no'.lower() or check=='n'.lower():
            break
    else:
        print('Invalid Input')
print('Thank you for using our service')