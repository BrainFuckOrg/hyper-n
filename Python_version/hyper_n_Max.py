def hyperN(number1, number2, n):
    if n == 1:
        return number1 + number2
    if number2 == 1:
        return number1
    return hyperN(number1, hyperN(number1, number2 - 1, n), n - 1);
