# test_figure.py
import unittest
from random import choice, randint
from app import Figure

class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.figure_type = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure_type, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        self.assertEqual(self.figure_type, self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(self.length, self.obj.get_figure_length)

    def test_obj_invalid(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_get_angles(self):
        if self.obj.type == "трикутник":
            self.assertEqual(self.obj.get_angles, 3)
        else:
            self.assertEqual(self.obj.get_angles, 4)

if __name__ == "__main__":
    unittest.main()
