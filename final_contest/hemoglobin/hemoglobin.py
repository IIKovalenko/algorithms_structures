
# coding: utf-8

# In[3]:


n = int(input())


# In[4]:


stack = []
sums = []


# In[5]:


sums.append(0)
for i in range(n):
    oper = input()
    if oper[0] is '+':
        x = int(oper[1:])
        stack.append(x)
        sums.append(sums[-1]+x)
    elif oper[0] is '-':
        sums.pop()
        x = stack.pop()
        print(x)
    elif oper[0] is '?':
        x = int(oper[1:])
        sum_last = sums[-1] - sums[-(1+x)]
        print(sum_last)

