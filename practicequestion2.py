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


