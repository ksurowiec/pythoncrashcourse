import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_text = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_text, 'Janis Joplin')

    def test_first_last_middle(self):
        formatted_text = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_text, 'Wolfgang Amadeus Mozart')


unittest.main()
