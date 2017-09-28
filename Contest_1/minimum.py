
# coding: utf-8

# In[1]:

class Stack_with_min:
    def __init__(self):
        self.a = []
        self.mins = []
    
    def push(self, element):
        self.a.append(element)
        if self.mins == []:
            self.mins.append(element)
        else:
            self.mins.append(min(element, self.mins[-1]))
    
    def pop(self):
        self.mins.pop()
        return self.a.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.a[-1]
        else: 
            pass
        
    def is_empty(self):
        return self.a == []
    
    def size(self):
        return len(self.a)
    
    def minimum(self):
        if not self.is_empty():
            return self.mins[-1]
        else: 
            pass
        
    def __call__(self):
        return self.a


# In[2]:

class Queue_of_stacks_with_min:
    
    def __init__(self):
        self.left_stack = Stack_with_min()
        self.right_stack = Stack_with_min()
        
    def enq(self, element):
        self.left_stack.push(element)
    
    def deq(self):
        if not self.right_stack.is_empty():
            self.right_stack.pop()
        else:
            while not self.left_stack.is_empty():
                self.right_stack.push(self.left_stack.pop())
            self.right_stack.pop()
    
    def minimum(self):
        mins = [x for x in [self.left_stack.minimum(), self.right_stack.minimum()] if bool(x)]
        return min(mins)
    
    def size(self):
        return len(self.__call__())
    
    def __call__(self):
        queue = self.right_stack.a[::-1] + self.left_stack.a
        return queue


# In[3]:

n, k = [int(s) for s in raw_input().split(' ')]


# In[11]:

array = [float(x) for x in raw_input().split(' ')]


# In[44]:

def get_minimums(array):
    queue = Queue_of_stacks_with_min()
    if array == []:
        return 0
    for i in xrange(n):
        queue.enq(array[i])
        if queue.size() == k:
            print(queue.minimum())
            queue.deq()
        i += 1


# In[47]:

get_minimums(array)


# In[ ]:



