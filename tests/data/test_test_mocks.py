import requests
import unittest
from unittest.mock import Mock

from requests.exceptions import ConnectionError, Timeout

requests = Mock()

def get_hoildays():
	r = requests.get("http://localhost/api/holidays")
	if r.status_code == 200:
		return r.json()
	return None


class TestGetHoildays(unittest.TestCase):

	def test_get_houldays_connections(self):
		requests.get.side_effect = ConnectionError
		with self.assertRaises(ConnectionError):
			get_hoildays()

	def test_get_houldays_timeout(self):
		requests.get.side_effect = Timeout
		with self.assertRaises(Timeout):
			get_hoildays()

	def log_request(self, url):
		print(f"Mocking a request to {url}")
		response_mock = Mock()
		response_mock.status_code = 200
		response_mock.json.return_value = {
			'25/12': 'Christmas',
			'01/01': 'New Year'
		}
		return response_mock

	def test_request_with_logging(self):
		requests.get.call_count = 0

		
		requests.get.side_effect = Timeout

		with self.assertRaises(Timeout):
			get_hoildays()

		## requests.get.side_effect = self.log_request("http://localhost/api/holidays")
		requests.get.side_effect = self.log_request

		assert get_hoildays()['25/12'] == 'Christmas'

		assert requests.get.call_count == 2

	

if __name__ == '__main__':
	#print(get_hoildays())
	unittest.main()