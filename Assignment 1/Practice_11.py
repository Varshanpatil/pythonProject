#Write a Python program to remove the nth index character from a non-empty string.

# Step 1: Define a function
def remove_character(string, n):
    # Step 2: Use slicing to remove the character
    return string[:n] + string[n+1:]

# Step 3: Example usage
text = "PythonProgramming"
index_to_remove = 6  # Index of the character to remove
result = remove_character(text, index_to_remove)

# Step 4: Print the result
print("Original string:", text)
print("After removing character at index", index_to_remove, ":", result)

#Explaination
#1.Define a Function: The remove_character function takes two arguments:
#string: The input string.
#n: The index of the character to remove.

#2.Slice the String:
#string[:n]: This gets all characters from the start of the string up to (but not including) the nth character.
#string[n+1:]: This gets all characters from the index after n to the end of the string.
#Concatenating these two parts (string[:n] + string[n+1:]) effectively removes the nth character.

#3.Use the Function: We pass the input string ("PythonProgramming") and the index of the character to remove (e.g., 6) to the function.

#4.Print the Result: The program displays the original string and the modified string with the character removed.