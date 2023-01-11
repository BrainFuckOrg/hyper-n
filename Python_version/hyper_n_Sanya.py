def hyper_n(num1, num2, grade):
    if grade == 1:
        return num1 + num2
    else:
        result = num1
        for i in range(1, num2):
            result = hyper_n(num1, result, grade - 1)
        return result
