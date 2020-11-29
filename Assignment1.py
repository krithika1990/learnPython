#!/usr/bin/env python
# coding: utf-8

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed  in a comma-separated sequence on a single line. 

# In[21]:


num=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        num.append(str(i))

print(','.join(num))


# Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name. 

# In[22]:


first_name =input("Enter your first name")
second_name = input("Enter your second name")
print(second_name + ' ' + first_name)


# Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3 

# In[25]:


rad = 12
pie=22/7
rad3= rad**3
v=4/3*pie*rad3
print(v)


# In[ ]:




