num = int(input('Enter the number:'))
count = 0
if num>1:
    for i in range(1,num+1):
        if (num%i==0):
            count+=1
    if count==2:
        print(f"Given number {num} is prime number")
    else:
        print(f'Given number {num} is not prime number')
