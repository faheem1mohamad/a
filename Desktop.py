#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello "faheem" khan")


# In[2]:


print("hellow \"faheem kahn'\ india")


# In[3]:


print ("faheem \"khan"\ king")


# In[4]:


print("king \"khan\" kinggg")


# In[7]:


print("/\\/\\/\\/\\/\\/\\ \t \"python is not a best \" and \" java is best \" ")


# In[6]:


num = int(input("enter the no."))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial) 


# In[10]:


num = int(input("Enter the value of n: "))
hold = num
sum = 0

if num <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
    print("Sum of first", hold, "natural numbers is: ", sum)


# In[13]:


num = int(input("enter the no "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[16]:


test_list = [5, 6, [6], 3, [], [], 9] 

print("The original list is : " + str(test_list)) 

res = [ele for ele in test_list if ele != []] 
  
print ("List after empty list removal : " + str(res)) 


# In[ ]:




