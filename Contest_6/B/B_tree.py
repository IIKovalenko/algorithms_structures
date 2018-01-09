
# coding: utf-8

# In[217]:


with open('tree.in') as f:
    data = f.read().split('\n')[:-1]
    N = int(data.pop(0))
    matrix = [[int(x) for x in string.split(' ')] for string in data]


# In[218]:


def make_graph_from_matrix(matrix):
    graph = [[] for i in range(N+1)]
    for idx, s in enumerate(matrix):
        for i, num in enumerate(s):
            if num is 1:
                graph[idx+1].append(i+1)
    return graph


# In[219]:


graph = make_graph_from_matrix(matrix)


# In[220]:


def DFS(graph, start):
    visited = set()
    stack = [start]
    color = [0]*(N+1)
    visited.add(start)
    while stack:
        current = stack.pop()
        color[current] = 'green'
        for v in graph[current]:
            if v not in visited:
                visited.add(v)
                color[v] = 'green'
                stack.append(v)
            else:
                if color[v] is 'green':
                    return('NO', visited)
        color[current] = 'red'
    return('YES', visited)


# In[221]:


all_vs = [x for x in range(1, N+1)]


# In[222]:


res = DFS(graph, 1)
if set(all_vs) - res[1]:
    answer = 'NO'
else:
    answer = res[0]


# In[223]:


with open('tree.out', 'w') as f:
    f.write(answer)

