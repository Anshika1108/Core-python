# Function to check if a string is a palindrome
def palindrome(string):
    string = string.replace("","").lower()
    return string == string[::-1]

user_input = input("Enter a string: ")

if palindrome(user_input):
    print(user_input, 'is a palindrome.')
else:
    print(user_input, "is not a palindrome.")
