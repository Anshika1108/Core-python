num = int(input('Enter the number = '))
factorial = 1
if num < 0 :
    print('factorial of 0 is does not exist')
elif num == 0 :
    print('factorial of 0 is 1')
elif num >0 :
     for i in range (1,num+1):
       factorial = i * factorial
print('factorial of',num,'is' ,factorial)