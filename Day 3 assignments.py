#!/usr/bin/env python
# coding: utf-8

# In[34]:


#Find all occurences of given list

def occurences(list1):
    list2 = [(i,list1.count(i)) for i in list1]
    print('Number','Occurences')
    for i in set(list2):
        print(i[0],'->',i[1])


# In[35]:


list1 = [1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]
occurences(list1)


# In[103]:


# Sort in terms of last digit of a string in list
def f1(str1):
    a = str1.split('.')
    b = []
    for i in a:
        b.append(int(i))
    return b[-1]


# In[104]:


list1 = ["192.168.10.9", "192.168.10.4", "192.168.10.11", "192.168.10.35"]
list1.sort(key = f1)
list1


# In[ ]:





# In[62]:


#append all the zeroes at the end of list
def Sort_zeroes(list1):
    list1.sort()
    for i in list1:
        if i ==0:
            list1.remove(i)
            list1.append(i)
    print(list1) 


# In[63]:


list1 = [1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]
Sort_zeroes(list1)


# In[ ]:





# In[64]:


# sort in terms of sum of tuple in the list

list1 = [(10,4),(90,3),(9,1),(10,4),(9,5)]
def fun1(x):
    return sum(x)
list1.sort(key = fun1)
print (list1)


# In[ ]:





# In[ ]:





# In[ ]:




