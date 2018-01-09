
# coding: utf-8

# In[144]:


with open('details.in') as f:
    data = f.read().split('\n')[:-1]
    times = [int(t) for t in data[0].split(' ')]
    details = [[] for i in range(len(times))]
    for idx, s in enumerate(data[1:]):
        details[idx] = [int(det) for det in s.split(' ') if s is not '']


# In[145]:


def DFS(arr, start, times):
    stack = [start]
    visited = set()
    time = 0
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(set(arr[current-1]) - visited)
            time += times[current-1]
    return time


# In[146]:


res = DFS(details, 1, times)


# In[135]:


with open('details.out', 'w') as f:
    f.write(str(res))

