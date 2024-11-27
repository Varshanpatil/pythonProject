#Write a program to check whether number is even or odd
num = int(input("Enter the number :"))

if num % 2==0:    #we used modulud,our no is divided and remainder should be 0 then it is even and if it is not 0 then it is odd
    print("Number is even")

else:
    print("Number is odd")