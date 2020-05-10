import unittest
import requests

class TestMain(unittest.TestCase):

	def test_catalog_book(self):

		# word not present in database 
		word = "test"
		result = requests.get("http://100.24.21.95:2002/catalog_book/{}".format(word))

		self.assertEqual(result.status_code,200)

		# word present in database
		word = "Barlaam and Ioasaph"
		result = requests.get("http://100.24.21.95:2002/catalog_book/{}".format(word))

		self.assertEqual(result.status_code,200)

	def test_catalog_author(self):

		# word not present in database
		word = "test"
		result = requests.get("http://100.24.21.95:2002/catalog_author/{}".format(word))

		self.assertEqual(result.status_code,200)

		# word present in database
		word = "Unknown"
		result = requests.get("http://100.24.21.95:2002/catalog_author/{}".format(word))

		self.assertEqual(result.status_code,200)

if __name__ == '__main__':
	unittest.main()