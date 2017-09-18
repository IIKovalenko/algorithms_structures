
# coding: utf-8

# In[23]:

import operator


# In[24]:

data = raw_input()


# In[25]:

data = data.split(' ')


# In[26]:

def poland(data):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = list()
    for element in data:
        if element in operators:
            a = stack.pop()
            b = stack.pop()
            stack.append(operators[element](float(b), float(a)))
        else: stack.append(element)
    return stack[-1]


# In[27]:

print(int(poland(data)))


# In[ ]:



