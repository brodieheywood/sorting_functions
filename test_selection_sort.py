from unittest import TestCase
from sorting_functions import selection


class TestSelectionSort(TestCase):
    def test_selection_smallest_case(self):
        unsorted = [1]
        sorted_copy = [1]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_zero(self):
        unsorted = [0]
        sorted_copy = [0]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_empty(self):
        unsorted = []
        with self.assertRaises(ValueError):
            selection.selection_sort(unsorted)

    def test_selection_general_case(self):
        unsorted = [3, 8, 5]
        sorted_copy = [3, 5, 8]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_negatives(self):
        unsorted = [-3, -8, -5]
        sorted_copy = [-8, -5, -3]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_mixed_negatives_and_positives(self):
        unsorted = [-3, 8, -5]
        sorted_copy = [-5, -3, 8]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_strings(self):
        unsorted = ['c', 'a', 'b']
        sorted_copy = ['a', 'b', 'c']
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_floats(self):
        unsorted = [3.3, 2.2, 1.1]
        sorted_copy = [1.1, 2.2, 3.3]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_negative_floats(self):
        unsorted = [-3.3, -1.1, -2.2]
        sorted_copy = [-3.3, -2.2, -1.1]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_negative_and_positive_floats(self):
        unsorted = [3.3, -2.2, 1.1]
        sorted_copy = [-2.2, 1.1, 3.3]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_mixed_floats_and_integers(self):
        unsorted = [1, 5.5, 3]
        sorted_copy = [1, 3, 5.5]
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_symbols(self):
        unsorted = ['V', 'd', '!', 'T', 'X', 'Q', 'q']
        sorted_copy = ['!', 'Q', 'T', 'V', 'X', 'd', 'q']
        self.assertEqual(sorted_copy, selection.selection_sort(unsorted))

    def test_selection_strings_and_integers(self):
        unsorted = ['a', 2, 'c', 4]
        with self.assertRaises(TypeError):
            selection.selection_sort(unsorted)

    def test_selection_strings_and_floats(self):
        unsorted = ['w', 1.1, 4.3, 'q']
        with self.assertRaises(TypeError):
            selection.selection_sort(unsorted)
