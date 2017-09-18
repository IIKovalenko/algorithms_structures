
# coding: utf-8

# In[34]:

brackets = raw_input()


# In[65]:

def check_brackets(brackets):
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    stack = []
    error = 0
    last_open = 0
    is_diff = False
    for bracket in brackets:
        if bracket in open_brackets:
            stack.append(bracket)
        if bracket in close_brackets:
            try: 
                last_open = stack.pop()
            except IndexError:
                error = 1
            if last_open != open_brackets[close_brackets.index(bracket)]:
                is_diff = True
    if error or (stack != []) or is_diff:
        answer = 'NO'
    else:
        answer = 'YES'
    return answer


# In[66]:

print(check_brackets(brackets))

