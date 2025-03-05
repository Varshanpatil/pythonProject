#Write a program to find the length of the string "machine learning" with and without using len function.

#With using len()-1 way
string_1 = "machine learning"
print(len("machine learning"))

#with using len()- 2 way
string_2 = ["machine learning"]
print(len(string_2[0]))


#without using len()
string_3 = ["machine learning "]
print(string_3[0].count("learning"))



