
# coding: utf-8

# In[89]:

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


# In[90]:

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

with open('crazycalc.in') as f:
    start, goal = [int(x) for x in f.read().split(' ')]


# In[106]:

def BFS(start, goal):
    start = start
    goal = goal
    queue = Queue_of_stacks()
    dist = [-1]*10001
    dist[start] = 0
    queue.enq(start)
    visited = {start}
    current = None
    while (queue.size() != 0) and (current is not goal):
        current = queue.deq()
        v1 = current*3
        v2 = current + sum([int(s) for s in str(current)])
        v3 = current-2
        for v in [v for v in (v1, v2, v3) if (v>=0 and v<10000)]:
            if v not in visited:
                queue.enq(v)
                dist[v] = dist[current] + 1
                visited.add(v)
    return dist[goal]


# In[107]:

res = BFS(start, goal)


# In[109]:

with open('crazycalc.out', 'w') as f:
    f.write(str(res))

