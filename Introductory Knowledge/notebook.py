#!/usr/bin/env python
# coding: utf-8

# # Commands
# * first introductionary steps 
# * press Alt + Enter or Shift + Enter to run the cell

# In[3]:


print("Hello World!")


# In[1]:


type(1)


# ## Calculations

# In[2]:


1+1


# In[3]:


1*2/3


# In[4]:


4**4 
# Use two asterisks to add an exponent


# In[8]:


5%2 
# The % sign gives the remainder of a divistion, given the division by integers


# ## How to Write + Lists and Sets

# In[1]:


"I don't like that"
# Brackets stay in the output


# In[12]:


print("Marmalade")


# In[14]:


print("My name is {}".format("Stefano"))
# Curly brackets are to be filled, with .format("")


# In[16]:


print("First: {x} Second: {y}".format(x="XXX", y="YYY"))
# You can change the value in the brackets


# In[17]:


["1","a","2","b","3","4"]
# List are used to store multiple items in a single variable


# In[2]:


mylist = ["AA","A","B"]
# Indexing in Python is a way to refer the individual items within an iterable by its position


# In[3]:


mylist[1]="A"
# Example: the first element of a List is indexed as 0, the second as 1, etc


# In[23]:


mylist


# In[5]:


mylist.append("C") 
# Add an element at the end of the list


# In[8]:


mylist
# Shows the content of the list


# In[38]:


mylist2 = [1, 2, ["A", "B"]]
# Nested list: a list inside a list (can be done many times)


# In[33]:


mylist2[2][1]
# Pick the second element in the third element of the nested


# In[44]:


t = (1,2,3)
# Tuple: a list that can't be changed (unmutable list)


# In[45]:


d = {"key1":"value1", "key2":"value2"}
# Dictionaries consist of a collection of key-value pairs, where each key-value pair maps the key to its associated value


# In[47]:


{1,2,3}
# Set = unordered collection of unique elements


# ## True or False? 

# In[58]:


1 > 4 
# Python checks if T-F and answers
# Usable with mathematical symbols like >, <, =, and their combinations


# In[59]:


1 == 1
# look for equality


# In[60]:


'A' == 'a'
# Valid also for words


# In[62]:


1 != 2
# Inequality


# ## Logical Operators

# In[66]:


1 < 2 and 3 > 1
# Better to use parenthesis to facilitate the reading


# In[69]:


(2 > 4) or (4 == 4)
# The logical operator "or" gives "true" if at least one condition is true


# In[76]:


if 1 == 2:
    print("worked")
else:
    print("not ok")
# Other logical operators: if - else conditions


# In[77]:


if 1 == 2:
    print("worked")
elif 3 == 3:
    print("eheh")
else:
    print("not ok")
# if - else conditions 


# In[13]:


seq = [1,2,3,4,5]
# Random list for the next command


# In[21]:


for x in seq:
    print("ciao %d" % (x))
# Loop: for - in; moreover, you can put whatever word you prefer instead of x


# In[12]:


i = 2
while i < 7:
    print("i is {}".format(i))
    i = i+1
# Loop: while  


# In[85]:


list(range(2,5))
# How to create a list starting from one element to another (not included)


# In[87]:


for x in range(5):
    print("hi")
# Loop: range can be used to set conditions inside the: for - in loops 


# In[90]:


x = [1,2,3,4,5,6]


# In[93]:


out =[]
for num in x:
    out.append(num**3)
    
print(out)

# 1 Create an empty list to be filled (here is OUT)
# 2 Create a loop from a starting list
# 3 Attach new elements to OUT (here is .append)
# 4 Far from the loop ask to see the list's content (print)


# In[96]:


[num**4 for num in x]
# Shortcut to do what we did above
# You only need x, and less typing


# ## Functions and Special Methods with Objects

# In[25]:


def my_func(name = "NO NAME"):
    print("Hello World! And Hello " + name)
# Here we define a new function (my_func) that requires an argument ("NO NAME" is not an argument)


# In[26]:


my_func("Stefano")
# If you forget the () then it will be shown where the function is stored, but the function won't be operated


# In[27]:


def square(x):
    return x**2
# Here we are defining a new function (again); "print" here is inappropriated: we want to define a function


# In[28]:


result = square(3)
# The "result" stores the result of the current operation


# In[29]:


result
# Try "type(result)" to see


# In[120]:


def times_two(var):
    return var*2
# Instead of defining a new function whenever wanted, call it Lambda: it is a one-shot function (see after)


# In[121]:


times_two(10)


# In[31]:


st = "hello my name is Stefano"
# String


# In[32]:


st.lower()
# Rewrite in lowercase


# In[132]:


st.upper()
# Rewrite in uppercase


# In[133]:


st.split()
# Separate any element of the string in a list


# In[136]:


tweet = "hello moto #motorola #bestphone"
# Suppose you deal with a post from Twitter or other platforms


# In[138]:


tweet.split()
# Separate any element of the string in a list based on the space (the empty brackets)


# In[140]:


tweet.split("#")
# Separate the strings' elements by #


# In[141]:


d = {"k1":"v1","k2":"v2"}
# Create a dictionary


# In[142]:


d.keys()
# Group the keys


# In[143]:


d.items()
# Group everything by relation (between a key and its element); no order between groups


# In[144]:


mylist = [1,2,3]


# In[149]:


first = mylist.pop(0)
# Create a variable "first" which is compound of the first element of "mylist"; "mylist" loses that element


# In[152]:


3 in mylist
# How to check if an element is in a list


# In[162]:


seq = ['soup','dog','salad','cat','great']
# Defined a sequence


# In[163]:


list(filter(lambda word: word[0]=="s", seq))
# Use the lambda (definable function) to search for a word that begins with s in sequence


# In[7]:


del mylist[4]
# Delete the selcted element from an list


# In[ ]:




