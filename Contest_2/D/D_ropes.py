
# coding: utf-8

# In[64]:


with open('ropes.in') as f:
    data = f.read().split('\n')
    n = int(data[0].split(' ')[0])
    k = int(data[0].split(' ')[1])
    ropes = [int(rope) for rope in data[1:-1]]


# In[65]:


def count_ropes(length):
    count = 0
    for rope in ropes:
        slices = rope//length
        count += slices
    return count


# In[74]:


def binary_search():
    answer = None
    L = 0
    R = sum(ropes)//k + 1
    while L+1 < R:
        mid = (L+R)//2
        if count_ropes(mid)-k >= 0:
            L = mid
        else:
            R = mid
    answer = L
    return answer


# In[75]:


with open('ropes.out', 'w') as f:
    f.write(str(binary_search()))

