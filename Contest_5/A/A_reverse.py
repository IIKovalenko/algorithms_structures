
# coding: utf-8

# In[277]:


with open('reverse.in') as f:
    data = f.read().split('\n')
    V = int(data[0])
    graph = []
    for vs in data[1:]:
        graph.append([int(v) for v in vs.split(' ') if vs is not ''])


# In[279]:


def reverse_orient_graph(graph):
    graph_reverse = [set() for i in range(len(graph))]
    for idx, vs in enumerate(graph):
        for v in vs:
            graph_reverse[v-1].add(idx+1)
    return graph_reverse


# In[280]:


reverse_graph = reverse_orient_graph(arr)


# In[281]:


output = str(V) + '\n'
for vs in reverse_graph:
    string = ''
    for v in vs:
        string += str(v) + ' '
    string = string.strip()
    output += string + '\n'


# In[282]:


with open('reverse.out', 'w') as f:
    f.write(output)

