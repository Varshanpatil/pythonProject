#Write a Python program to change a given string to a new string where the first and last characters have been exchanged.
def swap_first_last(string):
    # Check if the string is empty or has only one character
    if len(string) <= 1:
        return string  # No swapping needed

    # Swap the first and last characters
    new_string = string[-1] + string[1:-1] + string[0]
    return new_string

# Example usage
input_string = "hello"
result = swap_first_last(input_string)
print("Original string:", input_string)
print("Modified string:", result)
