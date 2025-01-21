# Function to check if a number is a palindrome
def palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

# Input from the user
num = int(input("Enter a number: "))
if palindrome(num):
    print(num," is a palindrome.")
else:
    print(num ,"is not a palindrome.")
