
# coding: utf-8

# In[5]:


with open('grasshopper.in') as f:
    data = f.read()
    n, k = [int(x) for x in data.split(' ')]


# In[232]:


def grasshopper(n, k):
    arr = [0]*(n+1)
    arr[0] = 1
    arr[1] = 1
    depth = 1
    if n>1:
        for i in range(2, min(k+1, len(arr))):
            arr[i] = 1 + sum(arr[i-depth:i])
            depth +=1
    if k<n:
        for i in range(k+1, n+1):
            arr[i] = sum(arr[i-depth:])
    return arr[n-1]


# In[235]:


with open('grasshopper.out', 'w') as f:
    f.write(str(grasshopper(n, k)))

