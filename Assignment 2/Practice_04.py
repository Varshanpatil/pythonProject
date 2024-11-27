#Write a program where user will get loan if it is having specific condition such as civil sscore,age,salary.
age = 30
salary = 60000
cibil_score = 400

if age > 20: #True
    print("Age is greater than 20")

    if salary > 50000:  #False
        print("Salary is greater than 50000")

        if cibil_score > 700 :
            print("Cibil score is greater than 700")
            print(("Loan Approved!"))
        else:
            print("Declined due to cibil score")

    else:
        print("Decliner due to salary")

else:
    print("Declined due to Age")