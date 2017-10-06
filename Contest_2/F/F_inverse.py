
# coding: utf-8

# In[22]:


with open('inverse.in') as f:
    data = f.read().split('\n')
    n = int(data[0])
    array = [int(x) for x in data[1].split(' ')]


# In[23]:


inverse_counter = 0


# In[27]:


def merge(left, right):
    merge_arr = []
    global inverse_counter
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merge_arr.append(left[i])
            i += 1
        else:
            merge_arr.append(right[j])
            j += 1
            inverse_counter += len(left) - i
    merge_arr = merge_arr + left[i:] + right[j:]
    return merge_arr


# In[28]:


def merge_sort(array):
    if len(array) > 1:
        idx = len(array)//2
        arr_left = array[:idx]
        arr_right = array[idx:]
        a = merge_sort(arr_left)
        b = merge_sort(arr_right)
        return merge(a, b)
    else:
        return array


# In[29]:


merge_sort(array)


# In[30]:


with open('inverse.out', 'w') as f:
    f.write(str(inverse_counter))

