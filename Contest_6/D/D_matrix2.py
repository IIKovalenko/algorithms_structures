
# coding: utf-8

# In[1]:


class Stack:
    
    def __init__(self):
        self.a = []
    
    def size(self):
        return len(self.a)
    
    def is_empty(self):
        return self.a == []
    
    def push(self, element):
        self.a.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.a.pop()
        else:
            pass
    
    def peek(self):
        if not self.is_empty():
            return self.a[-1]
        else: 
            pass


# In[2]:


class Queue_of_stacks:
    
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()
        
    def enq(self, element):
        self.left_stack.push(element)
    
    def deq(self):
        if not self.right_stack.is_empty():
            return self.right_stack.pop()
        else:
            while not self.left_stack.is_empty():
                self.right_stack.push(self.left_stack.pop())
            return self.right_stack.pop()
    
    def size(self):
        return len(self.__call__())
    
    def __call__(self):
        queue = self.right_stack.a[::-1] + self.left_stack.a
        return queue


# In[3]:


with open('matrix2.in') as f:
    data = f.read().split('\n')[:-1]
    pairs = []
    for pair in data:
        pairs.append([int(x) for x in pair.split(' ')])
    N, M = pairs.pop(0)


# In[4]:


def get_graph(pairs):
    graph = [[] for x in range(N+1)]
    for pair in pairs:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    return graph


# In[5]:


graph = get_graph(pairs)


# In[6]:


'''def BFS(graph, start, used):
    visited = set()
    queue = Queue_of_stacks()
    visited.add(start)
    used[start] = True
    queue.enq(start)
    while queue.size():
        current = queue.deq()
        for v in graph[current]:
            if v not in visited:
                visited.add(v)
                used[v] = True
                queue.enq(v)
    return visited'''


# In[7]:


def DFS(graph, start, used):
    visited = set()
    stack = [start]
    visited.add(start)
    used[start] = True
    while stack:
        current = stack.pop()
        for v in graph[current]:
            if v not in visited:
                visited.add(v)
                used[v] = True
                stack.append(v)
    return(visited)


# In[8]:


components = []
counter = 0
all_vs = [x for x in range(1, N+1)]
used = [False]*(N+1)
for v in all_vs:
    if not used[v]:
        comp = DFS(graph, v, used)
        components.append(comp)
        counter += 1


# In[9]:


answer = ''
answer += str(counter) + '\n'
for component in components:
    answer += str(len(component)) + '\n'
    s = ''
    for c in component:
        s += str(c) + ' '
    s = s[:-1]
    answer += s + '\n'
answer = answer[:-1]


# In[10]:


with open('matrix2.out', 'w') as f:
    f.write(answer)

