import unittest
import hello_world

class HelloTestCase(unittest.TestCase):
    def test_hello(self):
        self.assertEqual("Hello World", hello_world.text())