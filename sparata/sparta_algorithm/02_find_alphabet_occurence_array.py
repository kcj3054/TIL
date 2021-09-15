input = "hello my name is sparta"
alpha = [0] * 26

# 파이썬의 ord 함수 -> 특정 문자를 아스키 코드 값으로 변환해주는 함수
# chr() 함수 -> 아스키코드 값을 문자로 변환해 주는 함수
def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    maxIdx = 0;
    maxVal = -1
    for char in string:
        if not char.isalpha():
            continue
        else:
            alpha[ord(char) - ord('a')] += 1 ;

        for index in range(len(alpha)):
            if maxVal < alpha[index]:
                maxVal = alpha[index], maxidx = index
        print(alpha[maxidx])
        return 0


result = find_max_occurred_alphabet(input)
print(result)
