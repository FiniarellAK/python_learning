"""Write a function integer_element_count, where the function gets a mixedList. By mixedList we mean a list which can
contain integers, floats, lists, tuples, sets. For example mixedList can be ["1", 1, "abc", 123, 124.6, ['123', 1,
45], (1, 2), 3456, 567]. You need to find the count of only integers ( doesn't matter nested integer or not ). In the
case of example mixedList we must get the answer 8 ( 1, 123, 1, 45, 1, 2, 3456, 567"""


def print_only_int(mixed_list):
    for element in mixed_list:
        if type(element) == int:
            print(element)


if __name__ == '__main__':
    mixed_list = ["1", 1, "abc", 123, 124.6, ['123', 1, 45], (1, 2), 3456, 567]
    print_only_int(mixed_list)
