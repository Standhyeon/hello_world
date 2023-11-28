A, B = input('문자열 A, 문자열 B를 입력하시오 : ').split(' ')

def overlap(str_A, str_B):
    overlap_position = 0
    for i in range(1, min(len(str_A), len(str_B)) + 1):
        if str_A[-i:] == str_B[:i]:
            overlap_position = i

    return str_A + str_B[overlap_position:]

C = overlap(A, B)
print(C)
