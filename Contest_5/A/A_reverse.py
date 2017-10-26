
# coding: utf-8

# In[22]:


with open('reverse.in') as f:
    data = f.read().split('\n')[:-1]
    V = int(data[0])
    graph = []
    for vs in data[1:]:
        graph.append([int(v) for v in vs.split(' ') if vs is not ''])


# In[23]:


def reverse_orient_graph(graph):
    graph_reverse = [[] for i in range(len(graph))]
    for idx, vs in enumerate(graph):
        for v in vs:
            graph_reverse[v-1].append(idx+1)
    return graph_reverse


# In[24]:


reverse_graph = reverse_orient_graph(graph)


# In[26]:


output = str(V) + '\n'
for vs in reverse_graph:
    string = ''
    for v in vs:
        string += str(v) + ' '
    string = string.strip()
    output += string + '\n'


# In[27]:


with open('reverse.out', 'w') as f:
    f.write(output)

