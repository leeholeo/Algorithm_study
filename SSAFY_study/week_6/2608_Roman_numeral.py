'''
노가다 force
로마->아라비안: 순회하며 확인하고 더하기
아라비안->로마: 큰 숫자 순으로 자르기
'''
def roman_to_arabian(roman_number):
    arabian_number = 0
    i = 0
    while i < len(roman_number):
        for j in range(NUMERAL_LENGTH):
            if roman_number[i:i+ROMAN_NUMERAL_LENGTH[j]] == ROMAN_NUMERAL[j]:
                i += ROMAN_NUMERAL_LENGTH[j]
                arabian_number += ARABIAN_NUMERAL[j]
                break
        else:
            return -1
    return arabian_number


def arabian_to_roman(arabian_number):
    roman_number = ''
    for i in range(NUMERAL_LENGTH):
        while arabian_number >= ARABIAN_NUMERAL[i]:
            roman_number += ROMAN_NUMERAL[i]
            arabian_number -= ARABIAN_NUMERAL[i]
    return roman_number


ROMAN_NUMERAL = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
ROMAN_NUMERAL_LENGTH = tuple([1, 2] * 6 + [1])
ARABIAN_NUMERAL = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
NUMERAL_LENGTH = len(ROMAN_NUMERAL)

a_arabian = roman_to_arabian(input())
b_arabian = roman_to_arabian(input())

sum_arabian = a_arabian + b_arabian
print(sum_arabian)
print(arabian_to_roman(sum_arabian))
