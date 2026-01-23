#!/usr/bin/python3
def one(s: str, i):
    if i >= len(s) or i < 0:
        return 0
    c = s[i]
    match c[0]:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
        case _:
            return 0


def roman_to_int(roman_string):
    res = 0
    i = 0
    while i < len(roman_string):
        a = one(roman_string, i)
        b = one(roman_string, i + 1)

        if b == 0:
            res += a
        elif b > a:
            res += b - a
            i += 1
        else:
            res += a
        i += 1
    return res


if __name__ == "__main__":
    print(roman_to_int("X"))
    print(roman_to_int("VII"))
    print(roman_to_int("IX"))
    print(roman_to_int("LXXXVII"))
    print(roman_to_int("DCCVII"))
