#Write program to find minimum number in four numbers
#print(min(2,3,8,7))
#print(min(3.14,-3,100,0))


#write progrm to find minimum numbers in below numbers
def minimum(a, b):
    if a <= b:
        return a
    else:
        return b


# Driver code
a = -1
b = 4
print(minimum(a, b))