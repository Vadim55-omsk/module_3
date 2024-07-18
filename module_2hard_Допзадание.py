n =int(input('Введите число от 3 до 20 '))
def find_password(n):
    result = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                str_pair = str(i) + str(j)
                result.append(str_pair)

    return result

myTuple = find_password(n)
x = " ".join(myTuple)

print(n, ' ', x)
