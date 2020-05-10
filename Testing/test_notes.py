import unittest
import requests

class TestMain(unittest.TestCase):

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
	
	def test_search_notes(self):

		# retrieving the notes for which the notes are available
		word = "Seven Men"
		result = requests.get("http://100.24.21.95:2003/searchnotes/{}".format(word))

		self.assertEqual(result.status_code,200)

		# retrieving the notes for which the notes are not available
		word = "Barlaam and Ioasaph"
		result = requests.get("http://100.24.21.95:2003/searchnotes/{}".format(word))

		self.assertEqual(result.status_code,200)

if __name__ == '__main__':
	unittest.main()

