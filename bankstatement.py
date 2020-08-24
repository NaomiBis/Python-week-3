#A employee bank statement

#ask for user details
name=input("please enter name \n")
surname=input("please enter surname\n")

#ask for account number
acc_number= int(input("please enter account number \n"))

#ask for salary
salary=int(input("Enter your salary (R) \n"))

#variables to hold the tax, pension and new salary
tax_salary=0
new_salary=0
pension_savings=0

#tax calculation function
def tax():
    tax_salary=((10/100)*(salary))
    return tax_salary

#pension calculation function
def pension():
    pension_savings=((15/100)*(salary))
    return pension_savings

#new salary calculation function
def new_amount():
    new_salary=salary-tax()-pension()
    return new_salary

#display all details
print("*********Python Bank Statement**********")
print("#######################################")
print ("Name: \t \t \t",name)
print("Surname: \t \t",surname)
print("Account Number: \t",acc_number)
print("Account type:"+" \t \t Savings")

print("--------------------------------------------")

print("Your current salary: \t (R)", salary)
print("Your taxed amount: \t (R)", tax())
print("Your pension amount: \t (R)", pension())

print("-----------------------------------------")

print("Your current available amount: \t (R)",new_amount())

print("---------------THANK YOU------------------")
