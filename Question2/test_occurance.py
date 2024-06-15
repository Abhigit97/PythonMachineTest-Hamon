import unittest
from file_count_code import f
class TestOccurance(unittest.TestCase):
    def test_empty_string(self):
        result = f('')
        self.assertEqual(result, {})

    def test_single_character_string(self):
        result = f('a')
        self.assertEqual(result, {'a': 1})

    def test_repeated_characters_string(self):
        result = f('aaabb')
        self.assertEqual(result, {'a': 3, 'b': 2})

    def test_mixed_characters_string(self):
        result = f('abcabc')
        self.assertEqual(result, {'a': 2, 'b': 2, 'c': 2})

    def test_numbers_and_letters_string(self):
        result = f('a1a2b1b2')
        self.assertEqual(result, {'a': 2, '1': 2, '2': 2, 'b': 2})

    def test_special_characters_string(self):
        result = f('a!a@b!b@')
        self.assertEqual(result, {'a': 2, '!': 2, '@': 2, 'b': 2})

    def test_empty_list(self):
        result = f([])
        self.assertEqual(result, {})

    def test_single_element_list(self):
        result = f(['a'])
        self.assertEqual(result, {'a': 1})

    def test_repeated_elements_list(self):
        result = f(['a', 'a', 'a', 'b', 'b'])
        self.assertEqual(result, {'a': 3, 'b': 2})

    def test_mixed_elements_list(self):
        result = f(['a', 'b', 'c', 'a', 'b', 'c'])
        self.assertEqual(result, {'a': 2, 'b': 2, 'c': 2})

    def test_numbers_and_letters_list(self):
        result = f(['a', 1, 'a', 2, 'b', 1, 'b', 2])
        self.assertEqual(result, {'a': 2, 1: 2, 2: 2, 'b': 2})

    def test_special_characters_list(self):
        result = f(['a', '!', 'a', '@', 'b', '!', 'b', '@'])
        self.assertEqual(result, {'a': 2, '!': 2, '@': 2, 'b': 2})

    def test_empty_tuple(self):
        result = f(())
        self.assertEqual(result, {})

    def test_single_element_tuple(self):
        result = f(('a',))
        self.assertEqual(result, {'a': 1})

    def test_repeated_elements_tuple(self):
        result = f(('a', 'a', 'a', 'b', 'b'))
        self.assertEqual(result, {'a': 3, 'b': 2})

    def test_mixed_elements_tuple(self):
        result = f(('a', 'b', 'c', 'a', 'b', 'c'))
        self.assertEqual(result, {'a': 2, 'b': 2, 'c': 2})

    def test_numbers_and_letters_tuple(self):
        result = f(('a', 1, 'a', 2, 'b', 1, 'b', 2))
        self.assertEqual(result, {'a': 2, 1: 2, 2: 2, 'b': 2})

    def test_special_characters_tuple(self):
        result = f(('a', '!', 'a', '@', 'b', '!', 'b', '@'))
        self.assertEqual(result, {'a': 2, '!': 2, '@': 2, 'b': 2})

if __name__ == '__main__':
    unittest.main()
