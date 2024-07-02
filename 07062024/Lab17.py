# Take the 2 int number from the user and we want to add them.
# We need to use the input() function.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# type conversion - str -> int -> ? int()
result = int(num1)+int(num2)
print(result)

#  + ->  int  sum operation
#  + -> str - concat
# int to str -> str()
# str to int -> int()

print(type(int(num1)))


#if we do like this it will concatinate
#num1 = input("Enter number 1")
#num2 = input("Enter number 2")
#a= num1+num2
#print(a)