
# coding: utf-8

# In[3]:

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
             self.a.pop(0)
        else:
            pass
    
    def __call__(self):
        return(self.a)


# In[8]:

N = int(input())


# In[9]:

data = [raw_input() for i in range(N)]


# In[10]:

def get_quit_times(data):
    exit = [0 for x in data]
    queue = Queue()
    time = 0
    not_in_queue = 0
    
    for idx, string in enumerate(data):
        string = string.split(' ')
        client_time = 60*int(string[0]) + int(string[1])
        client_wait = int(string[2])
        time = client_time
        
        while (not queue.is_empty()) and (queue()[0] <= time) :
            a = queue.deq()
        
        if client_wait < queue.size():
            exit_time = client_time
            exit[idx] = '{} {}'.format(exit_time/60, exit_time%60)
            continue
            #print('{} {}'.format(client_hour, client_min))
        elif queue.is_empty():
            exit_time = client_time + 20
            queue.enq(exit_time)
            exit[idx] = '{} {}'.format(exit_time/60, exit_time%60)
        else: 
            exit_time = queue()[-1] + 20
            queue.enq(exit_time)
            exit[idx] = '{} {}'.format(exit_time/60, exit_time%60)
            
    return exit


# In[11]:

for time in get_quit_times(data):
    print(time)


# In[ ]:



