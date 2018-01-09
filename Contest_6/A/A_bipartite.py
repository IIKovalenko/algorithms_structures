
# coding: utf-8

# In[392]:


with open('bipartite.in') as f:
    data = f.read().split('\n')[:-1]
    pairs = []
    for pair in data:
        pairs.append([int(x) for x in pair.split(' ')])
    N, M = pairs.pop(0)


# In[393]:


def get_graph(pairs):
    graph = [[] for x in range(N+1)]
    for pair in pairs:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    return graph


# In[394]:


all_vs = []
for vs in pairs:
    all_vs += vs
all_vs = list(set(all_vs))


# In[395]:


graph = get_graph(pairs)


# In[396]:


def DFS(graph, start):
    visited = set()
    stack = [start]
    color = [0]*(N+1)
    color[start] = 1
    visited.add(start)
    while stack:
        current = stack.pop()
        for v in graph[current]:
            if color[v] == color[current]:
                return('NO', visited)
            if v not in visited:
                color[v] = -color[current]
                stack.append(v)
                visited.add(v)
    return('YES', visited)


# In[397]:


answers = []
left = list(all_vs)
while left:
    dfs = DFS(graph, list(left)[0])
    answers.append(dfs[0])
    left = set(left) - dfs[1]
answers = [answer == 'NO' for answer in answers]


# In[398]:


if M is 0:
    answer = 'YES'
else:
    if any(answers):
        answer = 'NO'
    else:
        answer = 'YES'


# In[399]:


with open('bipartite.out', 'w') as f:
    f.write(answer)

