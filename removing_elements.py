import unittest
# def fun(x):
#     return x + 1

# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3), 4)

def remove_every_other(my_list):
    # Your code here!
    # just make a list of every even index
    return [my_list[index] for index in range(0, len(my_list)) if index % 2 == 0]
    
class MyTests (unittest.TestCase):
    def test1(self):
        self.assertEqual(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),['Hello', 'Hello Again'])
    def test2(self):
        self.assertEqual(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])
    def test3(self):
        self.assertEqual(remove_every_other([[1, 2]]), [[1, 2]])
    def test4(self):
        self.assertEqual(remove_every_other([['Goodbye'], {'Great': 'Job'}]),[['Goodbye']])

if __name__ == '__main__':
        unittest.main()