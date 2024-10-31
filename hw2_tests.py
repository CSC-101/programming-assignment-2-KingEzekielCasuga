import data
import hw2
import unittest

from data import Duration, Point, Rectangle, Song
from hw2 import shorter_duration_than, validate_route, longest_repetition, create_rectangle, song_shorter_than, \
    running_time


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_create_rectangle_1(self):
        input1 = Point(2, 2)
        input2 = Point(10, 10)
        result = create_rectangle(input1, input2)
        expected = Rectangle(Point(2, 10), Point(10, 2))
        self.assertEqual(result, expected)

    def test_create_rectangle_2(self):
        input1 = Point(3, 2)
        input2 = Point(4, -3)
        result = create_rectangle(input1, input2)
        expected = Rectangle(Point(3, 2), Point(4, -3))
        self.assertEqual(result, expected)

    # Part 2

    def test_shorter_duration_than_1(self):
        input1 = Duration(3, 43)
        input2 = Duration(2, 12)
        result = shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(result, expected)

    def test_shorter_duration_than_2(self):
        input1 = Duration(1, 43)
        input2 = Duration(2, 12)
        result = shorter_duration_than(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    def test_shorter_duration_than_3(self):
        input1 = Duration(2, 43)
        input2 = Duration(2, 12)
        result = shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(result, expected)

    def test_shorter_duration_than_4(self):
        input1 = Duration(2, 1)
        input2 = Duration(2, 12)
        result = shorter_duration_than(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    # Part 3

    def test_song_shorter_than_1(self):
        input1 = [Song('The Beatles', 'Let it Be', Duration(4, 2)),
                  Song('Radiohead', 'Karma Police', Duration(4, 24)),
                  Song('Frank Ocean', 'White Ferrari', Duration(4, 2))]
        input2 = Duration(4, 20)
        result = song_shorter_than(input1, input2)
        expected = [Song('The Beatles', 'Let it Be', Duration(4, 2)),
                  Song('Frank Ocean', 'White Ferrari', Duration(4, 2))]
        self.assertEqual(result, expected)

    def test_song_shorter_than_2(self):
        input1 = [Song('The Beatles', 'Let it Be', Duration(4, 2)),
                  Song('Radiohead', 'Karma Police', Duration(4, 24)),
                  Song('Frank Ocean', 'White Ferrari', Duration(4, 2))]
        input2 = Duration(3, 1)
        result = song_shorter_than(input1, input2)
        expected = []
        self.assertEqual(result, expected)


    # Part 4

    def test_running_time_1(self):
        input1 = [Song('The Beatles', 'Let it Be', Duration(4, 2)),
                  Song('Radiohead', 'Karma Police', Duration(4, 24)),
                  Song('Frank Ocean', 'White Ferrari', Duration(4, 2))]
        input2 = [0, 2]
        result = running_time(input1, input2)
        expected = Duration(8, 4)
        self.assertEqual(result, expected)

    def test_running_time_2(self):
        input1 = [Song('The Beatles', 'Let it Be', Duration(4, 2)),
                  Song('Radiohead', 'Karma Police', Duration(4, 24)),
                  Song('Frank Ocean', 'White Ferrari', Duration(4, 2))]
        input2 = [1, 1, 1]
        result = running_time(input1, input2)
        expected = Duration(13, 12)
        self.assertEqual(result, expected)

    def test_running_time_3(self):
        input1 = [Song('The Beatles', 'Let it Be', Duration(4, 2)),
                  Song('Radiohead', 'Karma Police', Duration(4, 24)),
                  Song('Frank Ocean', 'White Ferrari', Duration(4, 2))]
        input2 = []
        result = running_time(input1, input2)
        expected = Duration(0, 0)
        self.assertEqual(result, expected)

    # Part 5

    def test_validate_route_1(self):
        input1 =[
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]
        input2 = ['san luis obispo', 'pismo beach']
        result = validate_route(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route_2(self):
        input1 =[
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'], ['pismo beach', 'atascadero']]
        input2 = ['san luis obispo', 'pismo beach', 'atascadero']
        result = validate_route(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route_3(self):
        input1 =[
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'], ['pismo beach', 'atascadero']]
        input2 = ['pismo beach']
        result = validate_route(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route_4(self):
        input1 =[
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'], ['pismo beach', 'atascadero']]
        input2 = ['pismo beach', 'santa margarita']
        result = validate_route(input1, input2)
        expected = False
        self.assertEqual(result, expected)

    # Part 6

    def test_longest_repetition_1(self):
        input = [1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 9]
        result = longest_repetition(input)
        expected = 5
        self.assertEqual(result, expected)

    def test_longest_repetition_2(self):
        input = [9, 9, 2, 2, 2, 2, 27, 3, 3, 3, 3, 2, 2]
        result = longest_repetition(input)
        expected = 2
        self.assertEqual(result, expected)

    def test_longest_repetition_3(self):
        input = [1]
        result = longest_repetition(input)
        expected = 0
        self.assertEqual(result, expected)

    def test_longest_repetition_4(self):
        input = []
        result = longest_repetition(input)
        expected = None
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
