def hyper_n(num1, num2, grade):
    if grade == 1:
        return num1 + num2
    else:
        result = num1
        for i in range(1, num2):
            result = hyper_n(num1, result, grade - 1)
        return result


def hyper_n_norecursion(num1, num2, grade):
    stack = [(num2, grade, 1)]
    result=num1
    count=0
    while len(stack) > 0:
        n2, g, i = stack.pop()
        if g == 1:
            result=num1+n2
        else:
            if i==1: result=num1
            if i<n2:
                stack.append((n2, g, i+1))
                stack.append((result, g-1, 1))
        #print(stack, result)
    return result
def tetration(num1, num2):
    result=num1
    for i in range(1, num2):
        result=num1**result
    return result