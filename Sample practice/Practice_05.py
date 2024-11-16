# Write a program to check if the word 'orange' is present in the "This is orange"
# Way 1
string_1 = "This is the Orange"
print(string_1[12:18])
print(string_1[12:])

# Way 2
# Define the string
string = "This is orange"

# check if orange is present
if "orange" in string:
    print("The word 'orange' is present")
else:
    print("The word 'orange' is not present")
