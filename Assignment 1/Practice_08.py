#How to access global variable
x = 10  # Global variable
y = 4

def modify_variable():
    global x  # Declare y as global
    y = 2
    y = y + 2  # Modify the global variable
    print("Inside function:", x)

modify_variable()
print("Outside function:", x)