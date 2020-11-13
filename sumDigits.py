def sumDigits(n):
    numString = str(n)
    result = 0
    for i in numString:
        result += eval(i)
    print(result)

sumDigits(1234)