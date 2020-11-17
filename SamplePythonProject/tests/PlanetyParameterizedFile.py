import unittest
from sample.Planety import *

class PlanetyParameterizedFile(unittest.TestCase):
    def test_from_file(self):
      fileTest = open("../data/planety_data_test")
      tmp = Planety()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp1, inp2, result = int(data[0]), data[1].strip("\n"), float(data[2].strip("\n"))
            self.assertEqual(tmp.newWiek(inp1, inp2), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
