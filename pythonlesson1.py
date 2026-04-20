#PRINTING
# normal print
print("Madhuja Tathe","first lesson")
# can print number directly
print(24)
#can add ,subtract, multiply , divide directly
print(24+67)
print(67-24)
print(12*5)
print(12/5)


# VARIABLES
name = "Maduja Tathe"
age = 18
price = 22.32
#apple and Apple is use as different variable
#printing
print("name") #this will print 'name'
print (name) #this will print 'madhuja tathe'
print ("my name is: ",name ,"and my age is :",age) #we can use statement and many variables

age2 = age
print(age2)
#we can use '_' 'a-z'
#can't write 1variable instead variable1, can't use number at start, can't use space 


# BASIC DATA TYPES
old = False
n = None
print(type(name))  #string('str')    (a-z) ('a' ,"a" ,'''a''')
print(type(age))   #integer('int')  (-ve,+ve,0)  (not2.5)
print(type(price)) #float('float')   (2.5, 5.6, 7.8)
print(type(old))   #boolean('bool') (True,False)  (T,F are capital)
print(type(n))     #none('nonetype') (N is capital)


#KEYWORDS
#they are reserve words in python (case sensitive)
# keywords : and else in return as except is True assert finally lambda try break False nonlocal with class for None while continue from not yield def global or del if pass elif import raise


# PRINTING SUM OF TWO NUMBERS
A = 2
B = 5
print("sum of two num. is: ",A+B)
sum =A+B
print("sum of two num. is: ",sum)

#COMMENT
#this symbol '#' is use to comment single line and for multiple line (""" asd""") or ('''asd''')
"""for 
commenting         shortcut key for comment is " ctrl+/ "
multiple 
line """


#BASIC DIFFERENT TYPES OF OPERATOR

#1.ARITHMETIC OPERATORS
#(+,-,*,/,%,**)
print(A+B)  #adding
print(A-B)  #subtracting
print(A*B)  #multiplying
print(A/B)  #dividing  (answer always come in floating value)
print(A%B)  #modulus (remainder)
print(A**B) #power operator (A^B)

#2.RELATIONAL OPERATORS (use in condition)
#(==,!=,<,>,<=,>=)
print(A==B)   #false (equal to)
print(A!=B)   #true  (not equal to)
print(A<=B)   #true  (less than and equal to)
print(A<B)    #true   (less than)
print(A>=B)   #false  (greater equal)
print(A>B)    #false  (greater)

#3.ASSIGNMENT OPERATOR
#(=,+=,-=,*=,/=,%=,**=)
num = 10 
num = num + 10      #10+10=20
num += 10          #above short form it is same
print("num: ", num) # num+10 =20; next line num(20 now)+=10 =30. therefore output is 30
# all the above are same as +=
a = 20
a = 10
print(a)

#4.LOGICAL OPERATOR ( work on boolean values )
#(not,and,or)
print(not False)   #not of false is true 
print(not (A>B))   #2>5 is false and its not is true
val1 = False
val2 = True
print("AND operator: ", val1 and val2)  #output will come as logic gates as per val1 and val2 is true or false
print("OR operator: ", (A==B) or (A>B)) # can use expression directly

#TYPE CONVERSION
#there are two type of conversion 

#1.TYPE CONVERSION (it is automatically done in python)
b = 4.25
print(a+b) #the conversion is done int to float 
# integers always convert to float value as float is superior

#if i write a = "2" this is string value
#           b= 4.25 it is float
#           print(a+b)
#str can't be added in float value error is given
#for this conversion to be done we use 2 type of conversion 

#2.TYPE CASTING
c = ("2")
c = float("2")   # we can also it into float by writing =float("2")
print(type(c))  #its type is now int
print(a+c)
# =float("madhuja") it will not get convert into float


#TAKING INPUT IN PYTHON
NAME = input("Enter your name: ")
print("welcome", NAME)
print(type(NAME))   #its output or give value is always in string
# for converting it into another type we have to use type casting
AGE = int(input("Enter your age:"))
PRICE = float(input("enter the price:"))
print(AGE)
print(PRICE)
print(type(AGE))    #its type is now int
print(type(PRICE))  #its type is now float

