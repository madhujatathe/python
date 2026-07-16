gggggg#LIST

#a built-in data type that stores set of values
#it can store elements if different types together(integer,float,string,etc)

#marks1 = 94.4  writting marks of every student by creating new variable and handling is also hard 
#marks2 = 87.3   therefore there is a built-in data type called list
#marks3 = 95.5
#marks4 = 66.9
marks = [94.4, 87.3, 95.5, 66.9]  #its a list 
#its always in square braket and seperated by ','.
print(type(marks))   #we can print type of a list
#in this we can access particular index like string
print(marks[0]) 
print(marks[3])     #marks of particular student can be accessed
print(len(marks))   #length of list 
#python's list is slightly diffent form array in c++ and java y
#in c++ and java we study arrays in which the data we store is generaly of same data type
#but in python list does not have this kinda rule
student = ["karan", 85, "Delhi"]  #ex
#string and list are kinda similar but it has a big difference in it to
#string are immutable and list are mutable in python (mutable can be change)
#in string we can access the value but cannot change the value 
#in list we can access the value and also can change the value of specified index
str = "hello"
print(str[0])    #this will error str object does not support item assignment
str[0] = "y"      

print(student[0])
student[0] = "arjun" #this will not give error and will change 
print(student)
