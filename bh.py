# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))



n = int (input (“Enter the number for which the factorial needs to be calculated: “)

factorial = 1

if n < 0:

              print (“Factorial cannot be calculated, non-integer input”)

elif n == 0:

              print (“Factorial of the number is 1”)

else:

              for i in range (1, n+1):

                             factorial = factorial *i

              print (“Factorial of the given number is: “, factorial
