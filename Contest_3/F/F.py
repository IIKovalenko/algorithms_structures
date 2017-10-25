
# coding: utf-8

# In[1]:


with open('input') as f:
    n = int(f.read())


# In[11]:


def count(n):
    arr = [0]*n
    if n is 1:
        return 2
    if n is 2:
        return 4
    arr[0] = 2
    arr[1] = 4
    arr[2] = 7
    for i in range(3, n):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    return arr[-1]


# In[7]:


with open('output', 'w') as f:
    f.write(str(count(n)))

