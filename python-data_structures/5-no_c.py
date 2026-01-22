#!/usr/bin/python3
def no_c(my_string):
    s = str()
    for c in my_string:
        if c.lower() != 'c':
            s += c
    return s


if __name__ == "__main__":
    print(no_c("CBest School"))
