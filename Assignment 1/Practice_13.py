#Write a program to find last 10 characters of a string?

def get_last_10_characters(string):
    # Return the last 10 characters using slicing
    return string[-10:]

# Example usage
input_string = "This is an example string to demonstrate the program."
result = get_last_10_characters(input_string)
print("Original string:", input_string)
print("Last 10 characters:", result)