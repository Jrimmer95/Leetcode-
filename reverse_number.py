def reverse(x: int) -> int:
    if x >= 0:
        x = str(x)
        y = ''
        y+=(x[::-1])
        if int(y) > (2**31)-1:
            return 0
        return int(y)
    elif x < 0:
        x = x * -1
        x = str(x)
        y = ''
        y+=(x[::-1])
        if -int(y) < -(2**31):
            return 0
        return -int(y)

print(reverse(120))
print(reverse(5681654615))
print(reverse(-1234567801))