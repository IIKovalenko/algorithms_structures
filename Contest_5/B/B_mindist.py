
# coding: utf-8

# In[106]:


with open('mindist.in') as f:
    data = f.read().split('\n')[:-1]
    V, s = [int(x) for x in data[0].split(' ')]
    matrix = []
    for string in data[1:]:
        matrix.append([int(x) for x in string.split(' ')])


# In[107]:


class Queue:
    
    def __init__(self):
        self.a = []

    def size(self):
        return len(self.a)
    
    def is_empty(self):
        return self.a == []
    
    def enq(self, element):
        self.a.append(element)
    
    def deq(self):
        if not self.is_empty():
             return self.a.pop(0)
        else:
            pass


# In[108]:


def BFS(matrix, s):
    s = s-1
    queue = Queue()
    queue.enq(s)
    dist = [-1]*V
    dist[s] = 0
    visited = {s}
    while (not queue.is_empty()):
        current = queue.deq()
        for idx, v in enumerate(matrix[current]):
            if v == 1 and (idx not in visited):
                visited.add(idx)
                dist[idx] = dist[current] + 1
                queue.enq(idx)
    return dist


# In[109]:


output = ''
for x in BFS(matrix, s):
    output += str(x) + ' '
output = output.strip()


# In[110]:


with open('mindist.out', 'w') as f:
    f.write(output)

