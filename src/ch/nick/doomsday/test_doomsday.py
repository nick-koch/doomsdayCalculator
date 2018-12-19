import unittest
from src.ch.nick.doomsday.doomsday import Doomsday

class MyTest(unittest.TestCase):
    def test_getTheCenturysAnchorday(self):

        res = Doomsday.getTheCenturysAnchorday(self, "0000")
        self.assertEqual(res, 2)
        res = Doomsday.getTheCenturysAnchorday(self, "0100")
        self.assertEqual(res, 0)
        res = Doomsday.getTheCenturysAnchorday(self, "0200")
        self.assertEqual(res, 5)
        res = Doomsday.getTheCenturysAnchorday(self, "0300")
        self.assertEqual(res, 3)

        res = Doomsday.getTheCenturysAnchorday(self, "0400")
        self.assertEqual(res, 2)
        res = Doomsday.getTheCenturysAnchorday(self, "0500")
        self.assertEqual(res, 0)
        res = Doomsday.getTheCenturysAnchorday(self, "0600")
        self.assertEqual(res, 5)
        res = Doomsday.getTheCenturysAnchorday(self, "0700")
        self.assertEqual(res, 3)

        res = Doomsday.getTheCenturysAnchorday(self, "0800")
        self.assertEqual(res, 2)
        res = Doomsday.getTheCenturysAnchorday(self, "0900")
        self.assertEqual(res, 0)
        res = Doomsday.getTheCenturysAnchorday(self, "1000")
        self.assertEqual(res, 5)
        res = Doomsday.getTheCenturysAnchorday(self, "1100")
        self.assertEqual(res, 3)

        res = Doomsday.getTheCenturysAnchorday(self, "1200")
        self.assertEqual(res, 2)
        res = Doomsday.getTheCenturysAnchorday(self, "1300")
        self.assertEqual(res, 0)
        res = Doomsday.getTheCenturysAnchorday(self, "1400")
        self.assertEqual(res, 5)
        res = Doomsday.getTheCenturysAnchorday(self, "1500")
        self.assertEqual(res, 3)

        res = Doomsday.getTheCenturysAnchorday(self, "1600")
        self.assertEqual(res, 2)
        res = Doomsday.getTheCenturysAnchorday(self, "1700")
        self.assertEqual(res, 0)
        res = Doomsday.getTheCenturysAnchorday(self, "1800")
        self.assertEqual(res, 5)
        res = Doomsday.getTheCenturysAnchorday(self, "1900")
        self.assertEqual(res, 3)

        res = Doomsday.getTheCenturysAnchorday(self, "2000")
        self.assertEqual(res, 2)
        res = Doomsday.getTheCenturysAnchorday(self, "2100")
        self.assertEqual(res, 0)
        res = Doomsday.getTheCenturysAnchorday(self, "2200")
        self.assertEqual(res, 5)
        res = Doomsday.getTheCenturysAnchorday(self, "2300")
        self.assertEqual(res, 3)

    def test_getTheDoomsdayOfYear(self):
        year = "1978"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 2)

        year = "2001"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 3)

        year = "1291"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 3)

        year = "0045"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 2)

        year = "7865"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 2)

        year = "1578"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 2)

        year = "2005"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 1)

        year = "1972"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 2)

        year = "1971"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 0)

        year = "1925"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 6)

        year = "1130"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 5)

        year = "5016"
        res = Doomsday.getTheDoomsdayOfYear(self, year, Doomsday.getTheCenturysAnchorday(self, year))
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()
