def str_to_list(str, trim):
    # Identify left and right boundaries first
    left = []
    right = []
    for c in str:
        if c == '[' or c == '(' or c == '{':
            left.append(c)
        elif c == ']' or c == ')' or c == '}':
            right.append(c)
        elif len(left) != 0 and len(right) != 0:
            break
    # Then extract the elements between the left and right boundaries
    rst = []
    flag = 0
    ele = ''
    i = 0
    while i < len(str):
        for l in left:
            if str[i] == l:
                flag += 1
                i += 1
        for r in right:
            if str[i] == r:
                flag -= 1
                i += 1
        if flag != 0:
            ele += str[i]
            i += 1
        else:
            rst.append(ele)
            ele = ''
            i += 1
    # Finally, illegal elements are removed
    ret = []
    for r in rst:
        for j in range(0, len(trim)):
            if r == trim[j]:
                break
            if j == len(trim) - 1 and r != trim[j]:
                ret.append(r)
    return ret