input = "abacabade"



def find_not_repeating_character(string):
    alpha = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alpha[arr_index] += 1;

    notRepeat = []
    for a in alpha:
        if a == 1:
            notRepeat.append(chr(a + ord('a') ))

    for char in string:
        if char in notRepeat:
            return char


result = find_not_repeating_character(input)
print(result)