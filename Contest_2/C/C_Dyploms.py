
# coding: utf-8

# In[271]:


from math import sqrt, floor


# In[272]:


with open('diplomas.in') as f:
    data = f.read().split(' ')
    w = int(data[0])
    h = int(data[1])
    n = int(data[2])


# In[273]:


def dyploms_left(a):
    ans = (a//h)*(a//w) - n
    return ans


# In[274]:


#(a//h)*(a//w) - столько дипломов вмещает квадрат со стороной а


# In[275]:


def binsearch():
    answer = None
    L = floor(sqrt(n*w*h))
    R = max(w, h)*n
    #from IPython.core.debugger import Tracer
    #Tracer()()
    while L+1 < R:
        mid = (L+R)//2
        if dyploms_left(mid)<0:
            L = mid
        else:
            R = mid
    answer = R
    return answer


# In[276]:


with open('diplomas.out', 'w') as f:
    f.write(str(binsearch()))

