
# coding: utf-8

# In[1]:


with open('father.in') as F:
    data = F.read().split('\n')[:-1]
    N = int(data[0])
    arr = []
    if N > 1:
        arr = [int(x) for x in data[1].split(' ')]


# In[2]:


def make_orient_graph(N, arr):
    graph = [[] for i in range(N+1)]
    for idx, emp in enumerate(arr):
        graph[emp].append(idx+2)
    return graph


# In[3]:


graph = make_orient_graph(N, arr)


# In[4]:


'''def DFS(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        current = stack.pop()
        for v in graph[current]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return(len(visited))'''


# In[5]:


#for i in range(1, N+1):
#    print(DFS(graph, i)-1)


# In[6]:


output = [0 for i in range(N+1)]
def get_sum(emp, output):
    summ = 0
    for i in graph[emp]:
        summ += get_sum(i, output) + 1
    output[emp] = summ
    return summ


# In[7]:


import sys
sys.setrecursionlimit(40000)


# In[8]:


get_sum(1, output)


# In[9]:


answer = ''
for i in range(1, N+1):
    answer += str(output[i]) + ' '


# In[10]:


answer = answer[:-1]


# In[11]:


with open('father.out', 'w') as F:
    F.write(answer)

