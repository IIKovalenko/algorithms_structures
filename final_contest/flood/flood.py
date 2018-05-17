
# coding: utf-8

# In[1]:


with open('flood.in') as F:
    data = F.read().split('\n')[:-1]
    A, B = [int(x) for x in data.pop(0).split(' ')]
    graph = [[] for i in range(B+2)]
    for st in data:
        s, f, h = [int(x) for x in st.split(' ')] 
        graph[s].append((f, h))
        graph[f].append((s, h))


# In[35]:


def DFS(graph, start, h):
    visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        current = stack.pop()
        for v in graph[current]:
            if (v[0] not in visited) and (v[1]>h):
                visited.add(v[0])
                stack.append(v[0])
    return(len(visited))


# In[39]:


def binary_search(graph, A):
    L = -1
    R = 10**6
    while L + 1 < R:
        mid = (L + R)//2
        if DFS(graph, 1, mid) < A:
            R = mid
        else:
            L = mid
    return R


# In[41]:


answer = binary_search(graph, A)


# In[43]:


with open('flood.out', 'w') as F:
    F.write(str(answer))

