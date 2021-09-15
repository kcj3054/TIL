input = [3, 5, 6, 1, 2, 4]

# 오메가는 1, o(n), -> 최선은 1, 최악은 n

def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for a in array:
        if a == number:
            return True;
    return False


result = is_number_exist(3, input)
print(result)