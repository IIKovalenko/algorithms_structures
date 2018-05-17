
# coding: utf-8

# In[1]:


with open('holidays.in') as F:
    data = F.read()
    N, M, w = [int(x) for x in data.split(' ')]


# In[11]:


def working_days(N, w, h):
    days_left = N - (N//(w+h))*(w+h)
    if days_left > w:
        return (N//(w+h) + 1)*w
    else:
        return (N//(w+h))*w + days_left


# In[15]:


def binary_search(N, M, w):
    L = 0
    R = 10**18
    while L + 1 < R:
        mid = (L + R)//2
        if working_days(N, w, mid) >= M:
            L = mid
        else:
            R = mid
    return L


# In[21]:


with open('holidays.out', 'w') as F:
    F.write(str(binary_search(N, M, w)))

