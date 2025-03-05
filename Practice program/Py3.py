#To find the largest number from given 3 numbers  a=10 , b=20 ,c= 30
#way-1
a = 10
b = 20
c = 30

#Need to compare each variable to other variable
if a > b and a > c:  #False and False ->False
    print("a is largest number")

elif b >a and b >c :  #True and False ->False
    print("b is largest number")

elif c >a and c > b:
    print("c is largest number")


