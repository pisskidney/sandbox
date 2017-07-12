import whois, mock
import unittest
import checkr


class TestCheckr(unittest.TestCase):
    def setUp(self):
        self.checkr = checkr.Checkr()

    def test_is_available_true(self):
        whois.query = mock.MagicMock(side_effect=Exception)
        self.assertEquals(True, self.checkr.is_available('foo.com'))

    def test_is_available_false(self):
        whois.query = mock.MagicMock(return_value='blabla')
        self.assertFalse(self.checkr.is_available('foo.com'))

    def test_word_to_domain_default(self):
        result = self.checkr.word_to_domain('abc')
        self.assertDictEqual(result, {'com': 'abc.com'})

    def test_word_to_domain_com_net(self):
        result = self.checkr.word_to_domain('abc', ['com', 'net'])
        self.assertDictEqual(result, {'com': 'abc.com', 'net': 'abc.net'})

    def test_word_to_domain_empty_list(self):
        result = self.checkr.word_to_domain('abc', [])
        self.assertDictEqual(result, {})
