
# coding: utf-8

# In[1]:

n, k = (int(x) for x in raw_input().split(' '))


# In[23]:

def counting(n, k):
    stack = [n]
    counter = 0
    while (stack != []) and (stack[-1] > k):
        up = round(stack[-1]/2.0)
        down = int(stack[-1]/2.0)
        stack.pop()
        stack.append(up)
        stack.append(down)
        while (stack != []) and (stack[-1] <= k):
            stack.pop()
            counter = counter + 1
    return counter


# In[25]:

print(counting(n, k))


# In[ ]:



