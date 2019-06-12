import unittest

def first_non_repeating_letter(string):

#     return the first item in a list of characters that are not repeating
#     if the list is empty, return an empty string
    new_string = string.lower()
    i = 0
    for letter in new_string:
        if new_string.count(letter) > 1:
            i+=1
            continue
        
        return string[i]
    return ''

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertEquals(first_non_repeating_letter('a'), 'a')
    def test2(self):
        self.assertEquals(first_non_repeating_letter(''), '')
    def test3(self):
        self.assertEquals(first_non_repeating_letter('abba'), '')
    def test4(self):
        self.assertEquals(first_non_repeating_letter('hello world, eh?'), 'w')

if __name__ == '__main__':
    unittest.main()