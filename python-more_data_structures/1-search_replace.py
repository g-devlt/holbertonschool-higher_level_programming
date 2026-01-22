#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [x if x != search else replace for x in my_list]


if __name__ == "__main__":
    print(search_replace([1, 2, 3, 2], 2, 99))
