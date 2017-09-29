
# coding: utf-8

# In[3]:

with open('ice-cream.in') as f:
    data = f.read().split('\n')
    data[0] = data[0].split(' ')
    n = int(data[0][0])
    k = int(data[0][1])
    coordinates = [int(x) for x in data[1].split(' ')]


# In[38]:

def can_be_placed(coordinates, mid):
    counter = 1
    pointer = 0
    distances = [coordinates[i] - coordinates[0] for i in range(1, n)]
    for idx, coordinate in enumerate(coordinates[pointer+1:]):
        distance = coordinate - coordinates[pointer]    
        if distance >= mid:
            pointer = idx
            counter += 1
    return counter >= k


# In[39]:

#distances = [coordinates[i] - coordinates[0] for i in range(1, n)]


# In[40]:

can_be_placed(coordinates, 99)


# In[41]:

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


# In[44]:

with open('ice-cream.out', 'w') as F:
    F.write(str(binary_search(coordinates)))

