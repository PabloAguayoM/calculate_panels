import unittest
from main import calculate_panels

class TestCalculatePanels(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(calculate_panels(1, 2, 2, 4), 4)

    def test_example_2(self):
        self.assertEqual(calculate_panels(1, 2, 3, 5), 7)

    def test_example_3(self):
        self.assertEqual(calculate_panels(2, 2, 1, 10), 0)

if __name__ == "__main__":
    unittest.main()