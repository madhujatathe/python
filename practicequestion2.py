#1.
#wap to input users first name & print its length
name = str(input("Enter your first name: "))
print(len(name))

#2.
#wap to find the occurrence of '$' in a string
str1 = "i have 10$ to 5$ bill"
print(str1.count("$"))

#3.
#grade student based on marks
markes = int(input("enter student marks: "))

if(markes >=90):
    grade = "A"
elif(marks >=80 and markes <90):
    grade = "B"
elif(marks >=70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("grade of the student ->", grade)

#4.
#wap to check if a number entered by the user is odd or even
num = int(input("enter a number"))

rem = num % 2
if(rem == 0):
    print("EVEN")
else:
    print("ODD")

#5.
#wap to find the greatest of 3 number entered by the user
a = int(input("enter a  first number"))
b = int(input("enter a  second number"))
c = int(input("enter a   third number"))

if(a >= b and a>= c):
    print("first number is largest",a)
elif(b >= c):
    print("second number is largest",b)
else:
    print("third is largest",c)
    

#6.
#wap to check if a number is a multiple of 7 or not
x = int(input("enter a number"))

if(x % 7 ==0):
    print("multiple of 7")
else:
    print("not a multiple")

