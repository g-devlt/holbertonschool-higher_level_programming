#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None: 
        return None
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print(new_in_list(a, 1, 10))
    print(a)
