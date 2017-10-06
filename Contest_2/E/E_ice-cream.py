
# coding: utf-8

# In[99]:


with open('ice-cream.in') as f:
    data = f.read().split('\n')
    data[0] = data[0].split(' ')
    n = int(data[0][0])
    k = int(data[0][1])
    coordinates = [int(x) for x in data[1].split(' ')]


# In[100]:


def can_be_placed(coordinates, mid):
    counter = 1
    pointer = 0
    for idx, coordinate in enumerate(coordinates):
        distance = coordinate - coordinates[pointer]
        if distance >= mid:
            pointer = idx
            counter += 1
    return counter >= k


# In[101]:


def binary_search(arr):
    answer = None
    L = 0
    R = arr[-1] - arr[0] + 1
    while L+1<R:
        mid = (L+R)//2
        if can_be_placed(arr, mid):
            L = mid
        else:
            R = mid
    answer = L
    return answer


# In[102]:


with open('ice-cream.out', 'w') as F:
    F.write(str(binary_search(coordinates)))

