def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def exponent(x,y):
    return x**y
def floar_div(x,y):
    return x//y
def check_remainder(x,y):
    return x%y
print('1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exponent\n6.Floor Division\n7.Check Remainder')
while True:
    choice = int(input('Enter the choice:'))
    if choice in (1, 2, 3, 4,5,6,7):
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
        elif choice==5:
            print(f"Exponent of {x} and {y} is:", exponent(x,y))
        elif choice==6:
            print(f"Floor Division of {x} and {y} is:", floar_div(x,y))
        elif choice==7:
            print(f"Remainder of {x} and {y} is:", check_remainder(x,y))
        check = input('Do you want to continue :[yes/no]')
        if check=='no'.lower() or check=='n'.lower():
            break
    else:
        print('Invalid Input')
print('Thank you for using our service')