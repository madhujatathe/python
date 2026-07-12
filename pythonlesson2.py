#STRING
#it's data type that stores a sequence of characters
#creating a string
str1 = "this is a string.\ncreating it in python."  #escape sequence charater like \n(next line),\t(tab-space)
print(str1)

#TYPE OF OPERATION

#CONCATENTION
#adding two string
#"hello"+"world"="helloworld"
str2 = "kitty"
str3 = "cat"
#printing lengt
print(len(str2))      #length is5
length = len(str3)    
print(length)        #length is3
print(str2+str3)
#printing length of added string
finalstring = (str2+" "+str3)   #in counting length charaters and space are also count
print(finalstring)
print(len(finalstring))    #length is 9 with a space

#INDEXING
#its a position of srting also count special charaters
#its use to access a charater
str = "apna college"
print(str[3])    #we can't replace any charater with the help of index
#str[4] = "_"  it will show error does not support item assignment

#SLICING

#
#accessing parts of a string
#str[starting index : ending index] where ending index is not included
print(str[1:4])   #pna is output
print(str[5:14])  #college is output
#if we have to write till last index we can also write
print(str[5:len(str)])
print(str[5:])   #if second no. is not written any thing it will take till last index
#the output for above will be the same i.e. "college"
print(str[:4])  #if fist no. is not written it will take 0

#negative silicing
print(str[-5:-2])


#DIFFERENT TYPE OF FUNCTION IN STRING

#1.                             #check the ending letter
print(str.endswith("ege"))      #its return true if string ends with sudstring(ege)
#2.                             #it is use for capitalize the first letter
print(str.capitalize())         #it doesn't change the main string
str4 = "i am stydying python"
str4 = str4.capitalize()        #for changing the main string this can be use
print(str4)
#3.                             #it is use for replacing a letter or a word 
print(str.replace("a","@"))
#4.                             #use to find a word or a letter
print(str4.find("p"))           #it return index of first letter
#if we write a letter which does not exist in string then it return (-1) and -1 is not a valid index
#negative index are only use for silicing normaly string are from 0
#5.                             #use for how many time word or letter comming in a string
print(str.count("a"))           


#CONDITIONAL STATEMENT

#1.if-elif-else

# Syntax
# if(condition):
#     statement1   
# elif(condition):
#     statement2
# else:
#     statementN
# it is use when you have many condition if the first condition is true then it will print otherwise check the next condition
# else is use if above all condition are false then statment in else will be print
ligth = "green"

if(light == "red"):
    print("stop")           #4space before statement is called indemtation
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")
 
print("end of code")
#we can make if and elif as many as we want but first if is compulsory then we can make as many as we want
#difference between if and elif is if condition is directly check it is true or false 
#and elif condition is only check after if condition is false so therefore atleast one if condition is compulsory
#else is only written once if above all condition are false it will print

 
