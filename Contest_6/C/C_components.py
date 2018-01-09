
# coding: utf-8

# In[33]:


with open('components.in') as f:
    data = f.read().split('\n')[:-1]
    N = int(data.pop(0))
    matrix = [[int(x) for x in string.split(' ')] for string in data]


# In[27]:


def make_graph_from_matrix(matrix):
    graph = [[] for i in range(N+1)]
    for idx, s in enumerate(matrix):
        for i, num in enumerate(s):
            if num is 1:
                graph[idx+1].append(i+1)
    return graph


# In[28]:


graph = make_graph_from_matrix(matrix)


# In[29]:


def DFS(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        current = stack.pop()
        for v in graph[current]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return(visited)


# In[30]:


all_vs = [x for x in range(1, N+1)]


# In[31]:


left = all_vs
counter = 0
while left:
    visited = DFS(graph, list(left)[0])
    counter += 1
    left = set(left) - visited


# In[34]:


with open('components.out', 'w') as f:
    f.write(str(counter))

