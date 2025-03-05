#will check load will approve to user or not
age = 25
salary = 65000
cibil_score = 550

if age > 20:  #True
    print("Age is grreater than 20")

    if salary > 50000: #True
        print('Salary is greater than 50000')

        if cibil_score > 750:  #True
            print("cibil score is greater than 750")
            print("Loan is approved")

        else:
            print("Declined due to cibil score")

    else:
        print("Declined due to salary")
        
else:
    print("Declined due to age")
