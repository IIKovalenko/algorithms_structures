
# coding: utf-8

# In[38]:


import sys

sys.setrecursionlimit(100500)


# In[39]:


with open('topsort.in') as f:
    data = f.read().split('\n')[:-1]
    pairs = []
    for pair in data:
        pairs.append([int(x) for x in pair.split(' ')])
    N, M = pairs.pop(0)


# In[40]:


def get_graph(pairs):
    graph = [[] for x in range(N+1)]
    for pair in pairs:
        graph[pair[0]].append(pair[1])
        #graph[pair[1]].append(pair[0])
    return graph


# In[41]:


graph = get_graph(pairs)


# In[42]:


def DFS(graph, s, color, arr):
    color[s] = 1
    for v in graph[s]:
        if color[v] is 0:
            DFS(graph, v, color, arr)
        elif color[v] is 1:
            arr.append(-1)
    color[s] = 2
    arr.append(s)


# In[43]:


color = [0]*(N+1)
arr = []
all_vs = [x for x in range(1, N+1)]


# In[44]:


for v in all_vs:
    if color[v] is 0:
        DFS(graph, v, color, arr)


# In[45]:


if min(arr) is -1:
    answer = str(-1)
else:
    arr.reverse()
    answer = ' '.join([str(x) for x in arr])


# In[46]:


with open('topsort.out', 'w') as f:
    f.write(answer)

