#Student Report program in python with **Kelly**

#ask the student for their name
student_name= input("please enter your name: \n")

#ask for the student for their surname
student_surname= input("please enter your surname: \n")

#ask student for their age, REMEMBER if input()
#functions always recieve strings (characters) so always convert it to an integer int()
student_age= int(input("please enter your age \n"))

#create a avarage variable to hold the total of the 3 marks and give it a value of 0
avarage_total = 0

#ask students for their 3 marks
subject_1= int(input("please enter mark for subject 1: \n"))
subject_2= int(input("please enter mark for subject 2: \n"))
subject_3= int(input("please enter mark for subject 3: \n"))

#this is the calculation that adds 3 numbers and divides it by 3
avarage_total = int(((subject_1+subject_2+subject_3) / 3))

#lets print and display the results
print("Student Name is:\n",student_name)
print("Student Surname is:\n",student_surname)
print("The total avarage mark is:\n",avarage_total)

#Advanced Challenge
#after calculating the avarage show the following:
#avarage less than 50 is a fail
#avarage equal to or more than 50 but less than 74 is a pass
#avarage equal and about 75 is a distinction

if avarage_total<50:
    print("Sorry, you have failed")

if avarage_total>= 50 and avarage_total<74:
    print("Welcome, you have passed")

if avarage_total>=75:
    print("Congradulations, you passed with a Distinction")
