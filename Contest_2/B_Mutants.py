
# coding: utf-8

# In[58]:

with open('mutants.in') as f:
    data = f.read().split('\n')
    N = int(data[0])
    if N is 0:
        mutants = []
    else:
        mutants = [int(x) for x in data[1].split(' ')]
    t = int(data[2])
    colors = [int(x) for x in data[3].split(' ')]


# In[59]:

def binsearch_first(array, element):
    answer = None
    L = -1
    R = len(array) - 1
    while L+1 < R:
        mid = (L+R)/2
        if array[mid] < element:
            L = mid
        else:
            R = mid
    if (array != []) and (element == array[R]):
        answer = R
    return answer


# In[60]:

def binsearch_last(array, element):
    answer = None
    L = 0
    R = len(array)
    while L+1 < R:
        mid = (L+R)/2
        if array[mid] > element:
            R = mid
        else:
            L = mid
    if (array != []) and (element == array[L]):
        answer = L
    return answer


# In[61]:

with open('mutants.out', 'w') as F:
    for color in colors:
        last = binsearch_last(mutants, color)
        first = binsearch_first(mutants, color)
        if (last or first) is None:
            F.write('0\n')
        else:
            F.write(str((last+1) - first) + '\n')

