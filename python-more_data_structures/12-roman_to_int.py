#!/usr/bin/python3
def one(s: str, i):
    if i >= len(s) or i < 0:
        return 0
    c = s[i]
    if c == 'I':
        return 1
    elif c == 'V':
        return 5
    elif c == 'X':
        return 10
    elif c == 'L':
        return 50
    elif c == 'C':
        return 100
    elif c == 'D':
        return 500
    elif c == 'M':
        return 1000
    else:
        return 0


def roman_to_int(roman_string):
    if(not isinstance(roman_string, str)):
        return 0
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
    print(roman_to_int(None))
    print(roman_to_int(10))
