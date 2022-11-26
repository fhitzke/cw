def armstrong_num(n):
    digits = [int(x)**len(str(n)) for x in str(n)]
    aNum = sum(digits)
    return aNum == int(n)