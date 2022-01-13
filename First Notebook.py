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


4**4 #exponents use two asterisks


# In[8]:


5%2 #the % gives the remainder of a divistion, 
#given the division by integers


# ## How to Write + Lists and Sets

# In[50]:


"i don't like that"
#brackets stays in the output


# In[12]:


print("Marmalade")


# In[14]:


print("My name is {}".format("Stefano"))
#the curly brackets are to be filled, with .format("")


# In[16]:


print("First: {x} Second: {y}".format(x="XXX", y="YYY"))
#you can change the value in the brackets


# In[17]:


["1","a","2","b","3","4"]
#list = arrays


# In[40]:


mylist = ["AAAAAAAA","AAAAAAAAAAAAAAAA","B"]
#indexed list


# In[31]:


mylist[1]="A"
#the first number is counted as 0, the second as 1, etc...


# In[23]:


mylist


# In[26]:


mylist.append("D") 
#add an element at the end of the list


# In[25]:


mylist


# In[38]:


mylist2 = [1, 2, ["A", "B"]]
#nested list


# In[33]:


mylist2[2][1]
#pick the second element in the third element of the nested


# In[44]:


t = (1,2,3)
#tuple = a list that can't be changed (unmutable list)


# In[45]:


d = {"key1":"value1", "key2":"value2"}
#dictionaries = hash tables; not a list, so no order


# In[47]:


{1,2,3}
#set = unordered collection of unique elements


# ## True or False? 

# In[58]:


1 > 4 
#Python checks if T-F and answers
#usable with any: >, <, =, and their combinations


# In[59]:


1 == 1
#look for equality


# In[60]:


'A' == 'a'


# In[62]:


1 != 2
#inequality


# ## Logical Operators

# In[66]:


1 < 2 and 3 > 1
#use parenthesis to facilitate reading


# In[69]:


(2 > 4) or (4 == 4)
#at least one is ok


# In[76]:


if 1 == 2:
    print("worked")
else:
    print("not ok")
#if - else conditions


# In[77]:


if 1 == 2:
    print("worked")
elif 3 == 3:
    print("eheh")
else:
    print("not ok")
#if - else conditions plus a second condition to be checked


# In[79]:


seq = [1,2,3,4,5]
#random list to show the next step


# In[81]:


for WHATEVER in seq:
    print(WHATEVER)
#you can actually put whatever word you prefer instead of WHATEVER


# In[84]:


i = 2
while i < 7:
    print("i is {}".format(i))
    i = i+1
#loops with "while"


# In[85]:


list(range(2,5))
#how to create a list from one element to another


# In[87]:


for x in range(5):
    print("hi")
#range is used to make stuff with "for x" 


# In[90]:


x = [1,2,3,4,5,6]


# In[93]:


out =[]
for num in x:
    out.append(num**3)
    
print(out)
#1 create an empty list to be filled (here is OUT)
#2 create a loop from a starting list
#3 attach new elements to OUT (here .append)
#4 far from the loop ask to see the list's content (print)


# In[96]:


[num**4 for num in x]
#a shortcut way to do what we did above
#you only need x, and less typing


# ## Functions and Special Methods with Objects

# In[110]:


def my_func(name = "NO NAME"):
    print("Hello World! And Hello " + name)
#here we simply define the function under a new name
#the "+banana" is another separated part of the function


# In[111]:


my_func("Stefano")
#if you forget the () then it will be shown where the 
#function is stored, but the function won't be operated


# In[115]:


def square(x):
    return x**2
#here are defining a new function again
#if we used "print", the "result" would not store anything


# In[116]:


result = square(3)
#the "result" stores the result of the current operation


# In[114]:


result
#try "type(result)" to see


# In[120]:


def times_two(var):
    return var*2
#instad of defining a new function whenever wanted, use 
#Lambda, which is a one-shot function (see after)


# In[121]:


times_two(10)


# In[126]:


st = "hello my name is Stefano"
#string


# In[131]:


st.lower()
#rewrite in lowercase


# In[132]:


st.upper()
#rewrite in uppercase


# In[133]:


st.split()
#separate any element of the string in a list


# In[136]:


tweet = "hello moto #motorola #bestphone"
#suppose you deal with Twitter


# In[138]:


tweet.split()
#separate any element of the string in a list


# In[140]:


tweet.split("#")


# In[141]:


d = {"k1":"v1","k2":"v2"}
#create a dictionary


# In[142]:


d.keys()
#group the keys


# In[143]:


d.items()
#group everything by relation (between a key and its element)
#no order between groups


# In[144]:


mylist = [1,2,3]


# In[149]:


first = mylist.pop(0)
#you create a variable "first" which is compound of the first
#element of "mylist". "mylist" loses that element


# In[152]:


3 in mylist
#how to check if an element is in a list


# In[162]:


seq = ['soup','dog','salad','cat','great']
#defined a sequence


# In[163]:


list(filter(lambda word: word[0]=="s", seq))
#use the lambda (definable function) to search for a word that 
#begins with s in sequence


# In[ ]:





# In[ ]:




