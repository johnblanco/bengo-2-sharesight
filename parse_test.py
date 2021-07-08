import unittest
from main import df_from_lines, read_file


class ParseTest(unittest.TestCase):

    def test_sndl(self):
        lines = read_file('sndl.txt')
        result = df_from_lines("SNDL", lines)

        buys = result[result['Transaction Type'] == 'BUY']

        self.assertEqual(3, len(buys))
        self.assertEqual(result.shape, (3, 10))


if __name__ == '__main__':
    unittest.main()
