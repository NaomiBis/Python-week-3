#A employee bank statment

#ask for user details
name = input("Please enter name \n")
surname= input("Please enter your surname")

#ask for account number
acc_number = int(input("Please enter account number \n"))

#ask for salary
salary = int(input("Enter your salary (R) \n"))

#variables to hold the tax, pension and new salary
tax_salary = 0
new_salary = 0
pension_savings = 0

#tax calculation function
def tax():
    tax_salary = ((10/100)*(salary))
    return tax_salary

#pension calculation function
def new_amount():
    new_salary = salary - tax() - pension()
    return new_salary

#display all details
print("*********** Python Bank Statment***********")
print("############################################")
print("Name: \t \t \t", name)
print("Surname: \t \t", surname)
print("Account Number: \t", acc_number)
print("Account Type: " + " \t \t Savings ")

print("---------------------------------------------")

print("Your current salary: \t (R)", salary)
print("Your taxed amount: \t (R)", tax())
print("Your prmsion amount: \t (R)", pension())

print("---------------------------------------------")

print("Your current availble amount: \t (R)", new_amount())\
            
print("---------------- THANK YOU ------------------")

      






