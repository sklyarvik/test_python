from functools import cmp_to_key
def compare(a, b):
    return (int(b + a) - int(a + b))


def largest_number(strings):
    sorted_strings = sorted(strings, key=cmp_to_key(compare))
    max_number = ''.join(sorted_strings)
    max_number = str(int(max_number))

    return max_number
lst = ['41', '4', '005', '89']
print(largest_number(lst))
