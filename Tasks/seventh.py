prime_number = int(input('enter the prime number = '))
def num(prime = prime_number):
        if prime <=1 :
            return False
        for i in range(2,prime):
              if prime % i == 0:
                  return False
        return True
print(num())

prime_num = int(input('enter the number = '))

if (prime_number<=1) or (prime_num % 2 == 0):
 print(prime_number,' is not a prime number')

else:
   print(prime_number, ' is a prime number')

