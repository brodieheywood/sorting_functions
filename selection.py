# Brodie Heywood
# November 26, 2018

"""Selection Sort"""

import doctest


def selection_sort(sortable_list):
    """Sort a list.

    Implements a simple search algorithm called selection sort.
    PARAM: sortable_list, a non-empty list of sortable items
    PRECONDITION: sortable_list cannot be empty; must contain sortable items (cannot be immutable). Can not evaluate
    strings with integers or floats.
    POSTCONDITION: sorts list items from lowest to highest value
    RETURN: a list; sorted copy of sortable_list
    >>> selection_sort([3])
    [3]
    >>> selection_sort([5, 0, 1, -4])
    [-4, 0, 1, 5]
    >>> selection_sort([-4, -2, -8])
    [-8, -4, -2]
    >>> selection_sort(['a', 'c', 'b'])
    ['a', 'b', 'c']
    >>> selection_sort([4.1, -2.1, 1.0])
    [-2.1, 1.0, 4.1]
    >>> selection_sort([1.5, 3])
    [1.5, 3]
    """
    sorted_copy = []

    if len(sortable_list) > 0:

        for i in range(len(sortable_list)):
            smallest_item = min(sortable_list)

            for item in sortable_list:
                if min(smallest_item, item) == item:
                    smallest_item = item
                else:
                    continue

            store = sortable_list.pop(sortable_list.index(smallest_item))
            sorted_copy.append(store)

        return sorted_copy

    else:
        print('The sortable_list parameter was empty.')
        raise ValueError


def main():
    unsorted = [3, 5, 1, 9, -4]
    sorted_copy = selection_sort(unsorted)
    print(sorted_copy)


if __name__ == '__main__':
    main()
    doctest.testmod()
