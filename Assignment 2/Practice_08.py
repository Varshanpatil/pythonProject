#Write a program to find the length of the string "machine learning" with and without using len function.
string = "machine learning"

#Using len() function
#count = len(string)
#print(count)

# Without using len() function
lenth_string = 0

for char in string:
    lenth_string += 1

print("Lenth without using len() :", lenth_string)
