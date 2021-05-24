import unittest
import random
from selection_sort import selection_sort


num_array = [i for i in range(1000)]

random.shuffle(num_array)

sorted_array = num_array
sorted_array.sort()

class SimpleTest(unittest.TestCase):
  
    #tests output of selection_sort against output of python's inbuilt sort. 
    def test_selection_sort(self):        
        self.assertEqual(sorted_array,  selection_sort(num_array) )
         
  
if __name__ == '__main__':
    unittest.main()
    