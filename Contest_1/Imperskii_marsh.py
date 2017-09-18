
# coding: utf-8

# In[1]:

N = int(raw_input())


# In[2]:

heights = [int(height) for height in raw_input().split(' ')]


# In[17]:

def count_sort(arr):
    a = arr
    mn = min(a)
    b = [0]*10000
    for num in a:
        b[num-mn] += 1
    answer = ''
    for i in xrange(10000):
        answer += (str(i+mn) + ' ')*b[i]
    return answer[:-1]


# In[20]:

print(count_sort(heights))

