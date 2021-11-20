import unittest
import os
import json
from http import HTTPStatus
from unittest.mock import patch

from app import create_app


class GetPhoneNumberTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.expect_data = {
            'formatted_phone_number': '(650) 810-1010'
        }

    @patch('app.service.GooglePlaceService.get_formatted_phone_number', return_value=(True, {
        'formatted_phone_number': '(650) 810-1010'
    }))
    def test_get_formatted_phone_number_successfully(self, _):
        response = self.client().get('/getphonenumber/?address=Computer%20History%20Museum%20Mountain%20View%20USA')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json, self.expect_data)

    def test_get_formatted_phone_number_empty_string_address(self):
        response = self.client().get('/getphonenumber/?address')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json.get('address'), ['Shorter than minimum length 1.'])

    def test_get_formatted_phone_number_missing_address(self):
        response = self.client().get('/getphonenumber/')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json.get('address'), ['Missing data for required field.'])

    @patch('app.service.GooglePlaceService.get_place_id', return_value=(False, None))
    def test_get_place_id_failed(self, _):
        response = self.client().get('/getphonenumber/?address=asdasd')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertEqual(response.json.get('message'), 'Cannot find phone number with this place')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
