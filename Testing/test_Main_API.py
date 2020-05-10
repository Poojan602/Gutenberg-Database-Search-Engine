import unittest
import requests

class TestMain(unittest.TestCase):
	
	def test_search_book(self):

		# book present in database
		book = "Seven Men"
		result = requests.get("http://100.24.21.95:2000/search_book/{}".format(book))

		self.assertEqual(result.status_code,200)

		# book not present in database
		book = "test"
		result = requests.get("http://100.24.21.95:2000/search_book/{}".format(book))

		self.assertEqual(result.status_code,200)

	def test_search_author(self):

		# author present in database
		author = "Max Beerbohm"
		result = requests.get("http://100.24.21.95:2000/search_author/{}".format(author))

		self.assertEqual(result.status_code,200)

		# author not present in database
		author = "test"
		result = requests.get("http://100.24.21.95:2000/search_author/{}".format(author))

		self.assertEqual(result.status_code,200)

	def test_search_notes(self):

		# retrieving the notes for which the notes are available
		word = "Seven Men"
		result = requests.get("http://100.24.21.95:2000/searchnotes/{}".format(word))

		self.assertEqual(result.status_code,200)

		# retrieving the notes for which the notes are not available
		word = "Barlaam and Ioasaph"
		result = requests.get("http://100.24.21.95:2000/searchnotes/{}".format(word))

		self.assertEqual(result.status_code,200)

	def test_submit_notes(self):

		# blank note submission
		word = "Barlaam and Ioasaph"
		note = " "
		result = requests.get("http://100.24.21.95:2003/submitnotes/{}/{}".format(word,note))

		self.assertEqual(result.status_code,200)

		# normal note submission
		word = "Barlaam and Ioasaph"
		note = "testing"
		result = requests.get("http://100.24.21.95:2003/submitnotes/{}/{}".format(word,note))

		self.assertEqual(result.status_code,200)

if __name__ == '__main__':
	unittest.main()