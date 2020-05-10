import unittest
import requests

class TestMain(unittest.TestCase):

	def test_log(self):

		word = "test"
		result = requests.get("http://100.24.21.95:2001/log/{}".format(word))

		self.assertEqual(result.status_code,200)

		word = " "
		result = requests.get("http://100.24.21.95:2001/log/{}".format(word))

		self.assertEqual(result.status_code,200)

if __name__ == '__main__':
	unittest.main()