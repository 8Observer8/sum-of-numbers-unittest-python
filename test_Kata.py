
import unittest
from Kata import Kata


class KataTest(unittest.TestCase):

    def test_add(self):
        # Arrange
        inputA = 5
        inputB = 6
        expected = 11

        # Act
        actual = Kata.Add(inputA, inputB)

        # Assert
        self.assertEqual(expected, actual)
