import requests
import json
import pytest

class TaskTwo():

    observatory_api_url = " Hong Kong Observatory API"

    payload = json.dumps({
        "args_one": "one",
        "args_two": "two",
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie':''
    }


    def send_request(self):
        observatory_response = requests.request(
            "POST", observatory_api_url, headers=headers, data=payload)
        return observatory_response.text

    # Test the request response status is whether successful or not
    def assert_responseCode(self):
        observatory_response = requests.request(
            "POST", observatory_api_url, headers=headers, data=payload)
        observatory_response_status = json.loads(observatory_response.text)['status']

        assert observatory_response_status == 'RightCode'


   
    def get_monday_humidity(self):
        observatory_response = self.send_request()
        monday_humidity = json.loads(observatory_response)['data']['Monday']['humidity']
        return monday_humidity

    '''
        Extract the relative humidity (e,g, 60 - 85%) for the day after tomorrow from the API
        response (e.g. if today is Monday, then extract the relative humidity for Wednesday)
    '''
    # according to real response then extract the relative humidity for the day after tomorrow,
    # code below is just an example
    def get_wednesday_humidity(self):
        observatory_response = self.send_request()
        monday_humidity = json.loads(observatory_response)['data']['Wednesday']['humidity']
        return monday_humidity

    
    def test_001(self):
        print('Test_01 folder\'s testCase assert_responseCode')
        with pytest.raises(AssertionError):
            self.assert_responseCode()


if __name__ == '__main__':
    tt = TaskTwo()
    tt.get_wednesday_humidity()
    pytest.main(['-v'])
