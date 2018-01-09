
# coding: utf-8

# In[7]:


with open('dijkstra.in') as f:
    data = f.read().split('\n')[:-1]
    N, s, f = [int(x) for x in data.pop(0).split(' ')]
    graph = [{} for x in range(N+1)]
    for idx, st in enumerate(data):
        graph[idx+1] = {i+1:int(v) for i, v in enumerate(st.split(' ')) if int(v) != -1}


# In[8]:


def get_min(d, visited):
    idx = 0
    for i in range(1, N+1):
        if d[i] < d[idx] and i not in visited:
            idx = i
    return idx


# In[9]:


def dijkstra(graph, s, f):
    d = [float('inf') for x in range(N+1)]
    d[s] = 0
    visited = set()
    
    current = s
    while d[current] < float('inf'):
        for v in range(1, N+1):
            minimum = get_min(d, visited)
            current = minimum
        
            visited.add(current)

            for v in graph[current].keys():
                    dist = d[current] + graph[current][v]
                    if dist < d[v]:
                        d[v] = dist
    
    if d[f] < float('inf'):
        answer = d[f]
    else:
        answer = -1
    
    return answer


# In[10]:


answer = dijkstra(graph, s, f)


# In[11]:


with open('dijkstra.out', 'w') as f:
    f.write(str(answer))

