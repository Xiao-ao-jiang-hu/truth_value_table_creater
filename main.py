input_str = input("与/\\,或\\/,非!,蕴含->,蕴含于<-,双蕴含<=> \n")
# replace signals into single character
replaced_str = input_str.replace("\\/", '+')
replaced_str = replaced_str.replace("/\\", '*')
replaced_str = replaced_str.replace("->", '>')
replaced_str = replaced_str.replace("<-", '<')
replaced_str = replaced_str.replace("<=>", '=')

char_list = list(replaced_str)

can = True
# check if there's unrecognizable characters
for i in replaced_str:
    if (i != '<') and (i != '*') and (i != '+') and (i != '>') and (i != '!') and (i != '=') and (i != '(') and (i != ')') and (not str.isalpha(i)):
        can = False
        break
if not can:
    print("wrong input")

# count variables and put them into list
variable_num = 0
variable_list = []
for i in replaced_str:
    if str.isalpha(i):
        variable_num += 1
        variable_list.append(i)
for i in variable_list:
    print(i, end="  ")
print(input_str)

# start from 000000……
binary_list = []
for i in range(0, variable_num):
    binary_list.append(0)

for i in binary_list:
    print(i, end="  ")
print(input_str)
# replace variables into numbers.
compute_list = char_list

# replace
for i in range(0, variable_num):
    for j in range(0, len(compute_list)):
        if compute_list[j] == variable_list[i]:
            compute_list[j] = binary_list[i]

# compute the value in a bracket
def compute_bracket(a_list):
    a_list.pop()
    a_list.pop(0)
    while len(a_list) > 1:
        for ind in range(0, len(a_list)-1):
            if a_list[ind] == '!':
                if not isinstance(a_list[ind+1], int):
                    print('wrong input. please check.')
                    return
                else:
                    a_list[ind+1] = int(not a_list[ind+1])
                    a_list.pop(ind)
                    return a_list
        for ind in range(0, len(a_list)-1):
            if a_list[ind] == '+':
                if not (isinstance(a_list[ind+1], int) or isinstance(a_list[ind-1], int)):
                    print('wrong input. please check.')
                    return
                else:
                    a_list[ind+1] = a_list[ind+1] or a_list[ind-1]
                    a_list.pop(ind-1)
                    a_list.pop(ind-1)
                    return a_list
        for ind in range(0, len(a_list)-1):
            if a_list[ind] == '*':
                if not (isinstance(a_list[ind+1], int) or isinstance(a_list[ind-1], int)):
                    print('wrong input. please check.')
                    return
                else:
                    a_list[ind+1] = a_list[ind+1] and a_list[ind-1]
                    a_list.pop(ind-1)
                    a_list.pop(ind-1)
                    return a_list

        for ind in range(0, len(a_list)-1):
            if a_list[ind] == '>':
                if not (isinstance(a_list[ind+1], int) or isinstance(a_list[ind-1], int)):
                    print('wrong input. please check.')
                    return
                else:
                    if a_list[ind+1]==0 and a_list[ind-1]==1:
                        a_list[ind + 1] = 0
                    else:
                        a_list[ind+1] = 1
                    a_list.pop(ind-1)
                    a_list.pop(ind-1)
                    return a_list

        for ind in range(0, len(a_list)-1):
            if a_list[ind] == '<':
                if not (isinstance(a_list[ind+1], int) or isinstance(a_list[ind-1], int)):
                    print('wrong input. please check.')
                    return
                else:
                    if a_list[ind+1] == 1 and a_list[ind-1] == 0:
                        a_list[ind + 1] = 1
                    else:
                        a_list[ind+1] = 0
                    a_list.pop(ind-1)
                    a_list.pop(ind-1)
                    return a_list

        for ind in range(0, len(a_list)-1):
            if a_list[ind] == '=':
                if not (isinstance(a_list[ind+1], int) or isinstance(a_list[ind-1], int)):
                    print('wrong input. please check.')
                    return
                else:
                    if a_list[ind+1]==a_list[ind-1]:
                        a_list[ind + 1] = 1
                    else:
                        a_list[ind+1] = 0
                    a_list.pop(ind-1)
                    a_list.pop(ind-1)
                    return a_list

        for ind in range(0, len(a_list)-1):
            if a_list[ind] == '=':
                if not (isinstance(a_list[ind+1], int) or isinstance(a_list[ind-1], int)):
                    print('wrong input. please check.')
                    return
                else:
                    if a_list[ind + 1] == a_list[ind - 1]:
                        a_list[ind + 1] = 1
                    else:
                        a_list[ind + 1] = 0
                    a_list.pop(ind - 1)
                    a_list.pop(ind - 1)
                    return a_list

stack = []
brackets = []
point = 0
# if the length of the list is not
while len(compute_list) != 0:
# from the index that point points, put it into the stack
    if_bracket = 0

    for i in compute_list:
        if i == '(' or i == ')':
            if_bracket = 1
    if if_bracket:
        while compute_list[0] != ')':
            stack.append(compute_list.pop(0))
            point += 1
        stack.append(compute_list[0])
        # put ) into the stack
        while stack[-1] != '(' or len(stack)==0:
            brackets.insert(0, stack.pop())
        brackets.insert(0, stack.pop())
        result = compute_bracket(brackets)
        stack.append(result[0])
        if stack[-1] != ')':
            stack.append(')')
        print(result)
        brackets=[]
    else:
        compute_list.insert(0, '(')
        compute_list.append(')')
        print(compute_list)
        print(compute_bracket(compute_list))






"""

(a/\(b/\c))/\(a/\b)



for i in compute_list:
    if i == '(' or i == ')':
        if_bracket = 1
if if_bracket:
    while compute_list[point] != ')':
        stack.append(compute_list[point])
        point += 1
    stack.append(compute_list[point])
    # put ) into the stack
    print(stack)
    while stack[-1] != '(':
        brackets.insert(0, stack.pop())
        point -= 1
    brackets.insert(0, stack.pop())
    result = compute_bracket(brackets)
    stack.append(result[0])
    print(stack)
    print(result)
else:
    compute_list.insert(0, '(')
    compute_list.append(')')
    print(compute_list)
    print(compute_bracket(compute_list))
    
"""