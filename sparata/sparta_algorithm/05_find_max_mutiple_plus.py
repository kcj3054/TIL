input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum = 0;
    for a in array:
        if a <= 1 or sum <= 1:
            sum += a
        else:
            sum *= a

    return sum


result = find_max_plus_or_multiply(input)
print(result)