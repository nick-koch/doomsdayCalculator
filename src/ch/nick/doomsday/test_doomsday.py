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


if __name__ == '__main__':
    unittest.main()
