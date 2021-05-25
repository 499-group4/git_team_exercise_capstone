import unittest
import random
from selection_sort import selection_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

import sys

sys.setrecursionlimit(1500)

num_array = [i for i in range(1000)]

random.shuffle(num_array)

sorted_array = num_array
sorted_array.sort()

num_array2 = num_array.copy()
sorted_array2 = num_array2
sorted_array2.sort()

num_array3 = num_array.copy()
sorted_array3 = num_array3
sorted_array3.sort()


class SimpleTest(unittest.TestCase):

    # tests output of selection_sort against output of python's inbuilt sort.
    def test_selection_sort(self):
        self.assertEqual(sorted_array, selection_sort(num_array))

    def test_quick_sort(self):
        self.assertEqual(sorted_array2, quick_sort(num_array2))

    def test_merge_sort(self):
        self.assertEqual(sorted_array3, quick_sort(num_array3))

    def test_insertion_sort(self):
        self.assertEqual(sorted_array, insertion_sort(num_array))
    
    def test_bubble_sort(self):
        self.assertEqual(sorted_array, bubble_sort(num_array))


if __name__ == '__main__':
    unittest.main()
