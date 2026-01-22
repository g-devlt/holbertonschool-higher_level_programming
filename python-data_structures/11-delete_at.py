#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None
    out = list()
    for i, x in enumerate(my_list):
        if i != idx:
            out.append(x)
    return out


if __name__ == "__main__":
    print(delete_at([1, 2, 3, 4], 2))
