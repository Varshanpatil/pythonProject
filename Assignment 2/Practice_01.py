#Python Program to find the largest element in the list

#way-1
# Step 1: Define a function to find the largest element
#def find_largest_element(numbers):
    # Step 2: Use the built-in max() function to find the largest
#    largest = max(numbers)
#    return largest

# Step 3: Example list of numbers
#numbers_list = [10, 45, 2, 78, 34, 56]

# Step 4: Call the function and store the result
#largest_number = find_largest_element(numbers_list)

# Step 5: Print the result
#print("The largest element in the list is:", largest_number)

#way-2-without using built in functions
def Find_max(list1):
    my_max = list1[0]

    for x in list1:
        if x>my_max:
            my_max=x
    return my_max

list1 = [5,15,30,4,100]
print("list1")

largest = Find_max(list1)
print("largest number in list is: ",largest)