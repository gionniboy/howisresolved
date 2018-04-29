#!/usr/bin/env python

import unittest
import howisresolved

class TestHowisresolved(unittest.TestCase):

    def test_validate_domain(self):
        domain = 'python.org'
        result = howisresolved.validate_domain(domain)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
