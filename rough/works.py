#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input())
if a%2==0:
    print("Even")
else:
    print("odd")


# In[12]:


a=int(input())
b=int(input())
c=int(input())
print(a,b,c,sep="-")
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


# In[18]:


num=int(input("Enter a number"))
if num==1:
    print("1")
else:
    while num>=1:
        print(num%2)
        num-=num


# In[21]:


def add(a,b):
    print(a+b)
add(1,2)


# In[29]:


#mult table
def table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
a=int(input("Enter the number "))
table(a)


# In[ ]:




