import unittest
import pytest

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


from bottles_classmethod_18 import BottleVerse, CountdownSong



class VerseRoleTest(unittest.TestCase):
    def assertPlaysVerseRole(self, role_player):
        self.assertTrue(hasattr(role_player, 'lyrics') and callable(role_player.lyrics))


class VerseFake:
    @staticmethod
    def lyrics(number):
        return f'This is verse {number}.\n'


class VerseFakeTest(unittest.TestCase):
    def test_plays_verse_role(self):
        tester = VerseRoleTest()
        tester.assertPlaysVerseRole(VerseFake)


class BottleVerseTest(unittest.TestCase):
    def test_plays_verse_role(self):
        tester = VerseRoleTest()
        tester.assertPlaysVerseRole(BottleVerse)

    def test_verse_general_rule_upper_bound(self):
        expected = (
            '99 bottles of beer on the wall, '
            '99 bottles of beer.\n'
            'Take one down and pass it around, '
            '98 bottles of beer on the wall.\n'
        )
        self.assertEqual(BottleVerse.lyrics(99), expected)

    def test_verse_general_rule_lower_bound(self):
        expected = (
            '3 bottles of beer on the wall, '
            '3 bottles of beer.\n'
            'Take one down and pass it around, '
            '2 bottles of beer on the wall.\n'
        )
        self.assertEqual(BottleVerse.lyrics(3), expected)

    def test_verse_7(self):
        expected = (
            '7 bottles of beer on the wall, '
            '7 bottles of beer.\n'
            'Take one down and pass it around, '
            '1 six-pack of beer on the wall.\n'
        )
        self.assertEqual(BottleVerse.lyrics(7), expected)

    def test_verse_6(self):
        expected = (
            '1 six-pack of beer on the wall, '
            '1 six-pack of beer.\n'
            'Take one down and pass it around, '
            '5 bottles of beer on the wall.\n'
        )
        self.assertEqual(BottleVerse.lyrics(6), expected)

    def test_verse_2(self):
        expected = (
            '2 bottles of beer on the wall, '
            '2 bottles of beer.\n'
            'Take one down and pass it around, '
            '1 bottle of beer on the wall.\n'
        )
        self.assertEqual(BottleVerse.lyrics(2), expected)

    def test_verse_1(self):
        expected = (
            '1 bottle of beer on the wall, '
            '1 bottle of beer.\n'
            'Take it down and pass it around, ' 
            'no more bottles of beer on the wall.\n'
        )
        self.assertEqual(BottleVerse.lyrics(1), expected)

    def test_verse_0(self):
        expected = (
            'No more bottles of beer on the wall, '
            'no more bottles of beer.\n'
            'Go to the store and buy some more, '
            '99 bottles of beer on the wall.\n'
        )
        self.assertEqual(BottleVerse.lyrics(0), expected)

class CountdownSongTest(unittest.TestCase):
    maxDiff = None

    def test_verse(self):
        expected = 'This is verse 500.\n'
        self.assertEqual(CountdownSong(verse_template=VerseFake).verse(500), expected)

    def test_verses(self):
        expected = (
            'This is verse 99.\n'
            '\n'
            'This is verse 98.\n'
            '\n'
            'This is verse 97.\n'
        )
        self.assertEqual(CountdownSong(verse_template=VerseFake).verses(99, 97), expected)

    def test_song(self):
        expected = (
            'This is verse 47.\n'
            '\n'
            'This is verse 46.\n'
            '\n'
            'This is verse 45.\n'
            '\n'
            'This is verse 44.\n'
            '\n'
            'This is verse 43.\n'
        )
        self.assertEqual(CountdownSong(verse_template=VerseFake, max=47, min=43).song(), expected)

