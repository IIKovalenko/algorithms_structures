
# coding: utf-8

# In[100]:

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


# In[101]:

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


# In[91]:

with open('mindist2.in') as f:
    data = f.read().split('\n')[:-1]
    V, E = [int(x) for x in data[0].split(' ')]
    start, goal = [int(x) for x in data[1].split(' ')]
    rebra = []
    for e in data[2:]:
        rebra.append([int(v) for v in e.split(' ')])


# In[92]:

def transform_to_list(rebra):
    arr = [[] for i in range(V)]
    for vs in rebra:
        arr[vs[0]-1].append(vs[1]-1)
        arr[vs[1]-1].append(vs[0]-1)
    return arr


# In[93]:

arr = transform_to_list(rebra)


# In[122]:

def BFS(arr, start, goal):
    start -= 1
    goal -= 1
    queue = Queue_of_stacks()
    dist = [-1]*V
    queue.enq(start)
    dist[start] = 0
    visited = {start}
    current = None
    pred = [[] for v in range(V)]
    pred[start] = -1 #нет предка у начальной в. обхода
    while (not queue.size() == 0) and (current is not goal):
        current = queue.deq()
        for v in arr[current]:
            if v not in visited:
                queue.enq(v)
                dist[v] = dist[current] + 1
                pred[v] = current
                visited.add(v)
    now = goal
    path = []
    path.append(goal+1)
    while(pred[now] != -1):
        now = pred[now]
        path.append(now+1)
    path.reverse()
    return (dist[goal], path)


# In[123]:

res = BFS(arr, start, goal)


# In[124]:

str_out = ''
for x in res[1]:
    str_out += str(x) + ' '


# In[125]:

with open('mindist2.out', 'w') as f:
    f.write(str(res[0]) + '\n' + str_out)

