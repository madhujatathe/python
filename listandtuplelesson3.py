#LIST    [basic, slicing, methods]

#a built-in data type that stores set of values
#it can store elements if different types together(integer,float,string,etc)

#marks1 = 94.4  writting marks of every student by creating new variable and handling is also hard 
#marks2 = 87.3   therefore there is a built-in data type called list
#marks3 = 95.5
#marks4 = 66.9
marks = [94.4, 87.3, 95.5, 66.9]  #its a list 
#its always in square braket and seperated by ','
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
#in string we can access the value but cann't change the value 
#in list we can access the value and also can change the value of specified index
str = "hello"
print(str[0])    #this will error str object does not support item assignment
str[0] = "y"      

print(student[0])
student[0] = "arjun" #this will not give error and will change 
print(student)
#in the above it contains indexing upto 2
print(student[4])
#if i write 3,4,etc indexing it will show error list index out of range

#LIST SLICING
#its similar to string slicing

#list name[starting index : ending index]         # we get a sublist

#ending index will not bw included in printing
print(marks[1:4])   #first three values will be printed 
#if we miss starting index it will automaticly take 0 index
#and if we miss ending index it will print till last index

#in list slicing we also have negative indexing like string
print(marks[-3:-1]) 

#LIST METHODS  [functions]
list = [2, 1, 3]

#basic function of list
#1.
list.append(4)            # adds one element at the end   [2, 1, 3, 4]

#2.
list.sort()               #sorts in  ascending order [1, 2, 3] (it will arrange in ascending order)
#ascending and descending

#3.
list.sort(reverse=true)   #sorts in descending order [3, 2, 1]

#4.
list.reverse()            # reverse list  [3, 1, 2]

#5. 
list.inster(idx,el)       #insert element at index   

 





