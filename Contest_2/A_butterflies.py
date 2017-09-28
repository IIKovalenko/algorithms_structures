
# coding: utf-8

# In[7]:

#N = int(raw_input())


# In[8]:

#collect = [int(x) for x in raw_input().split(' ')]
#comment_new

# In[9]:

#t = int(raw_input())


# In[10]:

#to_check = [int(x) for x in raw_input().split(' ')]


# In[ ]:

with open('collect.in') as F:
    data = F.read()
    data = data.split('\n')


# In[ ]:

N = int(data[0])
collect = [int(x) for x in data[1].split(' ')]
t = int(data[2])
to_check = [int(x) for x in data[3].split(' ')]


# In[11]:

def binary_search(array, element):
    answer = None
    L = -1
    R = len(array)-1
    while L+1 < R:
        mid = (L+R)/2
        if array[mid] < element:
            L = mid
        else:
            R = mid
    if (array != []) and (element == array[R]):
            answer = R
    return answer


# In[12]:

'''for number in to_check:
    if binary_search(collect, number) == None:
        print('NO')
    else:
        print('YES')'''


# In[ ]:

with open('collect.out', 'w') as F:
    F.write('')
    for number in to_check:
        if binary_search(collect, number) != None:
            F.write('YES\n')
        else:
            F.write('NO\n')

