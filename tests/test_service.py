import unittest
from unittest import mock

from app import GooglePlaceService
from conf import GOOGLE_API_KEY, GOOGLE_PLACE_URL


class ServiceTestCase(unittest.TestCase):

    @mock.patch('requests.request')
    def test_get_original_place_data_from_google_api(self, mock_get):
        mock_response = mock.Mock()
        # Define response data from Google API
        expected_dict = {
            "candidates": [
                {
                    "place_id": "ChIJm7NJkla3j4AR8vR-HWRxgOo"
                }
            ],
            "status": "OK"
        }

        # Define response data for my Mock object
        mock_response.json.return_value = expected_dict
        mock_response.status_code = 200

        # Define response for the fake API
        mock_get.return_value = mock_response

        # Call the function
        result = GooglePlaceService.get_place_id('test123')

        self.assertEqual(result, (True, 'ChIJm7NJkla3j4AR8vR-HWRxgOo'))
        mock_get.assert_called_with('GET',
                                    GOOGLE_PLACE_URL +
                                    '/findplacefromtext/json?input={input}&inputtype=textquery&fields={fields}&key={apiKey}'.format(
                                        input='test123', fields='place_id',
                                        apiKey=GOOGLE_API_KEY))

        GooglePlaceService.get_formatted_phone_number('test123')
        mock_get.assert_called_with('GET',
                                    GOOGLE_PLACE_URL +
                                    '/details/json?place_id={place_id}&fields={fields}&key={apiKey}'.format(
                                        place_id='ChIJm7NJkla3j4AR8vR-HWRxgOo', fields='formatted_phone_number',
                                        apiKey=GOOGLE_API_KEY))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
