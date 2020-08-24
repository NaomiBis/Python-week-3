#using functions

#ask for 2 numbers
num1=int(input("Number 1 \n"))
num2=int(input("NUMBER 2 \n"))

#a total variable to store our calculation
total=0
 #multiplication function
def multiplication():
    total= num1*num2
    return total
              
#subtraction function
def subtraction():
    total=num1-num2
    return total
    
         
  #addition function
def addition():
    total= num1+num2
    return total
          

 #division fuction
def division():
    total=num1/num2
    return total
         

 #displaying results
print("The 2 numbers multiplied are:",multiplication())
print("The 2 numbers subracted are:",subtraction())
print("The 2 numbers added are:",addition())
print("The 2 numbers divided are:",division())
                
