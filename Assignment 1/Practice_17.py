#Write a Python program to remove a newline in Python.

# Given string with a newline
#string = "Hello World\n"
#Method 1: Using strip() (Removes Leading & Trailing Newlines)
# Remove newline
new_string = string.strip()
print("Before:", string)  # Will print with a newline
print("After:", new_string)  # Newline removed

#Method 2: Using replace() (Removes All Newlines in the String)
string = "Hello\nWorld\nPython"
new_string = string.replace("\n", "")

print("Before:", string)  # Original string has newlines
print("After:", new_string)  # Newlines removed

#Method 3: Using rstrip() (Removes Only Trailing Newlines)
string = "Hello World\n\n"
new_string = string.rstrip("\n")

print("Before:", string)  # Original string has extra newlines at the end
print("After:", new_string)  # Newlines at the end removed