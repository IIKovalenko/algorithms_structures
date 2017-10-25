
# coding: utf-8

# In[17]:


with open('input') as f:
    data = f.read()
    n, m = [int(x) for x in data.split(' ')]


# In[18]:


def count_ways(n, m):
    if n<3 or m<3:
        if (n*m == 6) or (n*m == 1):
            return 1
        else:
            return 0
    else:
        arr = [[0]*m for i in range(n)]
        arr[0][0] = 1
        arr[2][1] = 1
        arr[1][2] = 1
        for i in range(2, n):
            for j in range(2, m):
                arr[i][j] = arr[i-2][j-1] + arr[i-1][j-2]
        return arr[n-1][m-1]


# In[19]:


with open('output', 'w') as f:
    data = f.write(str(count_ways(n, m)))

