def to_binary(n):
    assert n >= 0
    if n == 1:
        return "1"
    return to_binary(int(n / 2)) + str(n % 2)

print(to_binary(100))