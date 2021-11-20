import requests
from conf import GOOGLE_PLACE_URL, GOOGLE_API_KEY


class GooglePlaceService:
    base_url = GOOGLE_PLACE_URL
    find_place_by_text_path = base_url + '/findplacefromtext/json?input={input}&inputtype=textquery&fields={fields}&key={apiKey}'
    get_formatted_phone_number_path = base_url + '/details/json?place_id={place_id}&fields={fields}&key={apiKey}'

    @classmethod
    def get_place_id(cls, input):
        response = requests.request("GET", cls.find_place_by_text_path.format(input=input, fields='place_id',
                                                                              apiKey=GOOGLE_API_KEY))
        if response.json().get('status') == 'OK':
            candidates = response.json().get('candidates')
            return True, candidates[0].get('place_id')
        return False, None

    @classmethod
    def get_formatted_phone_number(cls, input):
        is_success, place_id = cls.get_place_id(input)
        if is_success:
            response = requests.request("GET",
                                        cls.get_formatted_phone_number_path.format(place_id=place_id,
                                                                                   fields='formatted_phone_number',
                                                                                   apiKey=GOOGLE_API_KEY))
            if response.json().get('status') == 'OK':
                return True, response.json().get('result')
        return False, 'Cannot find phone number with this place'
