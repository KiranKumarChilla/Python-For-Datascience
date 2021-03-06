
# coding: utf-8

# # Python For Data Science
# 
# “Torture the data, and it will confess to anything.”
# – Ronald Coase
# 
# Grateful to Mr.Guido van Rossum, Creator of Python who made our lifes easy.
# 
# This Notebook is continuation of my previous notes (PythonNotes1) on Python basics from Data Science perspective.
# 
# Topics covered
# 1. Arithmetic operators
# 2. Relational operators
# 3. Logical operators
# 4. Assignment operators
# 5. Identity operators
# 5. if elif else statements
# 6. Loops
# 7. break vs continue
# 8. Functions
# 9. lambda expressions
# 10. lambda vs functions
# 11. Map
# 12. filter
# 13. reduce
# 14. List Comprehensions
# 
# Will soon post the new files with topics including generators, files, classes, exception handling, Numpy, Pandas, etc.., 

# ## Operators
# 

# ### Arithmetic operators

# In[1]:


a= 100
b =15
# addition 
result = a+b
print("result after adding a and b is", result)
# subtraction
result = a-b
print("result after subtracting a and b is", result)
#multiplication
result = a*b
print("result after multiplying a and b is", result)
#Division
result = a/b
print("result after Dividing a and b is", result)
# modulus
result = a%b
print("result after  a modulus b is", result)


# In[2]:


#The "+" can also be used to concatenate two strings or lists
list_1 = ['d','a','t']
list_2 = ['a','_','M','L']
result = list_1 + list_2
print(result)
## To know more about lists and strings please refer my pythonNotes1


# ### Difference between division operators : "/" vs "//"

# In[3]:


num1 = 80
num2 = 7
#Division(float):"/"
result = num1/num2
print("result after subtracting a and b is", result)
#Division(floor):"//"
result = num1 // num2
print("result after subtracting a and b is", result)


# ### Relational Operators
# It compares values and returns True or False

# Eg: consider ">", 
# 
# greater than denoted by > (it returns true if A is greater than B in "A > B" else, it returns false ) where A and B can be integer or string

# In[4]:


1 > 2


# In[5]:


1 < 2


# In[6]:


1 >= 1


# In[7]:


1 <= 4


# In[8]:


1 == 1


# ### String comparison using relational operators
# Strings are compared using ASCII value of the characters
# 
# If A and B are strings ; then it compares each element from left to right till both elements in A and B are different, then it compares the ASCII value of those two unique elements.

# In[9]:


A = "Data"
B = "science"

print("Output for A(Data)>B(Science) is", " ", A>B)
print("Output for A(Data)<B(Science) is", " ", A<B)


# In[10]:


# It returns false because the first unique element of two strings are 'd' and
#'s'As ASCII value of "d" (in string "data") is less than "s" (in string "sci")
'datas'>'sci'


# In[11]:


'datas' == 'sci'


# In[12]:


'datas' != 'sci'


# ### Logical Operators
# and
# 
# or
# 
# not

# In[13]:


# A and B returns true if both expression A and B returns True else returns false
(1 > 2) and (2 < 3)


# In[14]:


# A and B returns true if atleast one of expression A and B is True else 
# returns false
(1 > 2) or (2 < 3)


# In[15]:


not((1 > 2) or (2 < 3))


# ### Assignment operators

# In[16]:


# "+=", Adds right side value to left side value and then assigns new value to 
# the left side variable
a = 10
b = 5
a+=b
print("value of a after performing a+=b is"," ",a)
# "-=", Subtracts right side value with leftside value and then assigns new value to 
# the left side variable

a = 10
b= 5
a-=b
print("value of a after performing a-=b is"," ",a)
# "*=", Multiplies right side value with leftside value and then assigns new value to 
# the left side variable
a = 10
b= 5
a *= b 
print("value of a after performing a*=b is"," ",a)
# "**=" calculates left side value raise to the power of right side value and assigns 
# it to leftside value
a = 10
b= 5
a **= b 
print("value of a after performing a**=b is"," ",a)


# ### Identity operators
# 
# "in" and "not in"

# In[17]:


#x"in" y :outputs true if it finds x in sequence Y, false otherwise


# In[18]:


X  =  2
Y = [1, 2, 3]
print("output for X(2) in Y([1, 2, 3]) is"," ",X in Y)


# In[19]:


#x"not in" y :outputs true if it finds x in sequence Y, false otherwise


# In[20]:


X  =  2
Y = [1, 2, 3]
print("output for X(2) not in Y([1, 2, 3]) is"," ",X not in Y)


# Extra Info:
# Apart from the above mentioned operators; Python also has
# 5. Bitwise operators
# 6. Membership operators
# 

# ## If elif else statements
# if condition:
#   
#   //code
# 
# elif condition:
#   
#   //code
#   
# else:
#   
#   //code

# In[21]:


a = 100
b = 50

if a > b:
    print("a>b")
elif(a == b):
    print("a=b")
else:
    print("a<b")


# In[22]:


number = int(input("enter number \n"))


# In[23]:


if(number >= 1 and number <= 10):
    print("number between 1 to 10")
elif(number >= 11 and number <= 20):
    print("number between 11 to 20")
elif(number >= 21 and number <= 30):
    print("number between 20 to 30")
else:
    print("number greater than 30")


# ## Loops:
# Loops are basically used when you have a certain part of code which has to be repeated for n number of times

# ### for loop: 
# 
# defined as
# 
# for i in iterable:
#         
#         code
# where iterable can be list or list of lists or defined by range(x) 

# In[24]:


my_list = range(3)


# In[25]:


for i in my_list:
    print(i)


# In[26]:


my_list = [1, 2, 3]


# In[27]:


for i in my_list:
    print(i)


# In[28]:


my_list = ['a', 'b', 'c']


# In[29]:


for i in range(len(my_list)):
    print (i)


# In[30]:


# nested for loops
for i in range(2):
    for j in range(2):
      print (i*j)


# In[31]:


#forloops and if statements
my_list = range(20)
even_list = []
odd_list = []

for i in my_list:
    if(i % 2 ==0):
        even_list.append(i)
    else:
        odd_list.append(i)

print('list of even numbers are', even_list)
print('list of odd numbers are',odd_list)


# In[32]:


numb_3 = []
numb_5 = []
numb_7 = []
numb_others =[]

for i in my_list:
    if(i % 3 ==0):
        numb_3.append(i)
    elif(i % 5 ==0):
        numb_5.append(i)
    elif(i % 7 ==0):
        numb_7.append(i)
    else:
        numb_others.append(i)


# In[33]:


numb_3


# In[34]:


numb_5


# In[35]:


numb_7


# In[36]:


numb_others


# ### while loop:
# defined as:
# 
# while condition:
#    
#      /code/ 
#     
# In contrast to far, while loop checks the condition for every iteration 

# In[37]:


count = 0
while count < 2:
    print("Data Science")
    count+=1


# In[38]:


# while and if statements)
even_list = []
odd_list = []
i=0
while i < 20:
    if(i % 2 ==0):
        even_list.append(i)
    else:
        odd_list.append(i)
    i+=1

print('list of even numbers are', even_list)
print('list of odd numbers are',odd_list)


# ### break vs continue; 
# break is used to when you want to end the loop if certain condition is met
# 
# continue is used if you don't want to run the entire loop for certain condition

# In[39]:


#here you want to come out of the loop once the sum becomes zero. 
#so, break is used
sum = 0
print('value for i is')
for i in range(-2, 4):
    sum = sum+i
    print(i)
    if(sum == 0):
        print('sum is equal to zero')
        break


# In[40]:


# Continue: Here you want to divide the  sum with i; Here you don't want to execute 
# the division statement only for i =0
print('value for i is')
for i in range(-2, 4):
    if(i == 0): 
        continue
    print(i,"\t")
    sum = sum/i


# ## List Comprehensions
# It is defined by List(expression (for loop with one or more conditions))

# In[41]:


list_1 = [j for j in range(4)]


# In[42]:


list_1


# In[43]:


#squaring the first 10 numbers; here we have only one condition
list_1 = [i*i for i in range(10)]


# In[44]:


list_1


# In[45]:


#Squaring the even numbers in first 10 numbers; here we have more than 
# one condition 
list_2 = [i*i for i in range(10) if i%2 == 0]


# In[46]:


list_2


# In[47]:


## nested for loops;  outer loop will be followed by inner loops

list_2 = [(j, k) for j in range(2) for k in range(2)]


# In[48]:


list_2


# In[49]:


list_2 = [j for j in range(4) for k in range(j)]


# In[50]:


list_2


# In[51]:


list_2 = [(j, k) for j in range(4) for k in range(j)]

list_2


# ## Functions
# function declaration: def keyword is used
# 
#  def func_name:  
#  
#      /code/

# In[52]:


# function definition
def my_function():
    print("Sample function definition")


# In[53]:


# function call
my_function()


# In[54]:


def add(a, b):
    return a+b


# In[55]:


add(20, 30)


# In[56]:


# nested loops


# ## Lambda expressions
# 
# It is defined as 
# 
# lambda arguments : expression
# 
# It can have any number of arguments but only once expression

# In[57]:


lambda_declaration = lambda x: x * 2


# In[58]:


lambda_declaration(4)


# In[59]:


#addition using lambda expressions and functions


# In[60]:


add = lambda x, y : x+y

def add_func(x, y):
    return(x+y)


# In[61]:


add(2, 3)


# In[62]:


add_func(2,3)


# ## lambdas vs functions
# 1. Lambda expressions can be used as a replacement for functions especially in case of operations between numbers.
# 2. Lambdas makes writing code a bit easier and a bit cleaner
# 3. lambda expressions are mainly used along with map, filter, reduce

# In[63]:


# factorial declaration in function
def factorial(x):
    if x == 1:
        return 1
    else:
        x= x-1
        return(x*factorial(x))


# In[64]:


# factorial declaration in lambda
factorial_lambda = lambda x:x ** 2


# In[65]:


print(factorial(2))


# In[66]:


factorial_lambda(8)


# ## map() 
# It is used to make transformations to the existing elements in datastructure
# 
# map is defined by  map(function, seq1, seq2,...);
# seq1, seq2 can be list or tuple or set or..

# In[67]:


list_1 = [1, 2, 3]
newlist_map = map(lambda x:x+2, list_1) 


# In[68]:


list(newlist_map)


# In[69]:


list_2 = ['data','science','machine','learning' ]


# In[70]:


newlist2_map = map(lambda x:x+" test", list_2)


# In[71]:


list_2


# In[72]:


list(newlist2_map)


# In[73]:


#performing operation on lists

list(map(lambda x,y:str(x) + " "+y , list_1, list_2))


# ## filter() 
# if you want to filter a data with some condition for example, suppose if you want to find only even numbers from a given list
# 
# defined as: filter(condition/filtering function, sequence)
# 
# sequence can be list or tuple or set
# 
# It also returns a sequence of elements; filter function can only have one iterable/sequence as input
# 

# In[74]:


list_1 = [1, 5, 4, 6, 8, 11, 3, 12]


# In[75]:


new_list = filter(lambda x: x%2 == 0 , list_1)


# In[76]:


print(list(new_list))


# In[77]:


list_2 = ['1', '5', '4', '6', '8', '11', '3', '12']


# In[78]:


new_list_2 = filter(lambda x: int(x)%2 == 0 , list_2)


# In[79]:


list(new_list_2)


# In[80]:


"right" >= "left"


# In[81]:


"right" < "rih"


# In[82]:


##List of dictionaries


# In[83]:


dict_list = [{1:'DataScience',2:'ml',3:'AI'},{1:'DataScience',2:'ml'}]


# In[84]:


even_dict = filter(lambda x:len(x)%2 == 0, dict_list)


# In[85]:


list(even_dict)


# ## reduce() ; 
# 
# It is used to return a single value from a given set of elements(list/sets/..)
# 
# It is defined by reduce(func, sequence)
# 
# Sequence can be list/set/tuple
# 
# func is the operation that needs to repeatedly performed on all elements in sequence

# In[86]:


import functools as fn
 
# importing operator for operator functions
import operator as op


# In[87]:


(fn.reduce(op.mul,list_1))


# In[88]:


(fn.reduce(op.add,list_2))


# 
# #### Any questions or suggestions, shoot me an email @ kirankchilla2@gmail.com
# ### Thank You
