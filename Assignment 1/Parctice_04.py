#Write a program to print every character of a string entered by the user in a new line using a loop

#Get string input from the user
user_var = input("Enter a string: ")

# Loop through each character in the string
for char in user_var:
    print(char)


#explaination
#1.Input from the User:
#The input() function is used to prompt the user to type something.Whatever the user types is stored as a string in the variable user_input.
#If the user enters Hello, the variable user_input will now hold the value "Hello".

#2.For Loop Starts:
#The for loop iterates through the string user_input character by character.
#char is a temporary variable that takes the value of each character in the string during each iteration of the loop.
#In the first iteration, char is "H".In the second iteration, char is "e".This continues until the last character of the string.

#3.Printing Each Character:
#The print() function is used to display the current character (char) on the screen.
#This happens for each character in the string as the loop iterates.