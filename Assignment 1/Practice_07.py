#How to access global variable
x = 10  # Global variable
y = 4

def modify_variable():
    global y  # Declare y as global
    y = 4
    x = y + 5  # Modify the global variable
    print("Inside function:", x)

modify_variable()
print("Outside function:", x)
