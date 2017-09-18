
# coding: utf-8

# In[77]:

N = int(raw_input())


# In[78]:

data = raw_input()


# In[79]:

scores = [int(score) for score in data.split(' ')]


# In[80]:

def swap(arr, left, right):
    a = arr
    t = a[left]
    a[left] = a[right]
    a[right] = t
    return a


# In[81]:

def insertion_sort(array):
    a = array
    indexes = [x+1 for x in range(len(a))]
    for i in range(len(a)):
        j = i
        while (j>0) and (a[j-1] > a[j]):
            swap(a, j-1, j)
            swap(indexes, j-1, j)
            j = j-1
        #print a
    return a, indexes


# In[82]:

sorted_scores = insertion_sort(scores)


# In[83]:

answer = ''
for score in sorted_scores[1][::-1]:
    answer = answer + str(score) + ' '


# In[88]:

print answer[:-1]


# In[ ]:



