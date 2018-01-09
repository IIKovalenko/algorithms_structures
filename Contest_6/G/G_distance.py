
# coding: utf-8

# In[92]:


with open('distance.in') as f:
    data = f.read().split('\n')[:-1]
    n, m = [int(x) for x in data.pop(0).split(' ')]
    s, f = [int(x) for x in data.pop(0).split(' ')]
    graph = [{} for x in range(n+1)]
    for e in data:
        v1, v2, dist = [int(x) for x in e.split(' ')]
        graph[v1][v2] = dist
        graph[v2][v1] = dist


# In[93]:


def get_min(d, visited):
    idx = 0
    for i in range(1, n+1):
        if d[i] < d[idx] and i not in visited:
            idx = i
    return idx


# In[94]:


def dijkstra(graph, s, f):
    d = [float('inf') for x in range(n+1)]
    d[s] = 0
    visited = set()
    pred = [0]*(n+1)
    pred[s] = None
    
    current = s
    while d[current] < float('inf'):
        for v in range(1, n+1):
            minimum = get_min(d, visited)
            current = minimum
        
            visited.add(current)

            for v in graph[current].keys():
                    dist = d[current] + graph[current][v]
                    if dist < d[v]:
                        d[v] = dist
                        pred[v] = current
    
    if d[f] < float('inf'):
        path = []
        vi = f
        while vi is not None:
            path.append(vi)
            vi = pred[vi]
        path.reverse()
        answer = str(d[f]) + '\n' + ' '.join([str(x) for x in path if x is not None])
    else:
        answer = '-1'
    
    
    return answer


# In[95]:


answer = dijkstra(graph, s, f)


# In[96]:


with open('distance.out', 'w') as f:
    f.write(answer)

