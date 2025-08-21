from unittest.mock import Mock, patch
from lib.time_error import TimeError
import time

def test_time_difference_with_mocks():

    requester_mock = Mock(name = "requester")
    response_mock = Mock(name = "response")

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {
        "utc_offset":"+01:00",
        "timezone":"Europe/London",
        "day_of_week":4,
        "day_of_year":233,
        "datetime":"2025-08-21T10:29:25.116606+01:00",
        "utc_datetime":"2025-08-21T09:29:25.116606+00:00",
        "unixtime":1755768565,
        "raw_offset":0,
        "week_number":34,
        "dst": True,
        "abbreviation":"BST",
        "dst_offset":3600,
        "dst_from":"2025-03-30T01:00:00+00:00",
        "dst_until":"2025-10-26T01:00:00+00:00",
        "client_ip":"5.67.146.80"
    }

    with patch('time.time', return_value = 1755770165): 
        time_error = TimeError(requester_mock)
        result = time_error.error()

    assert result == (1755768565 - 1755770165)

"""    
patch is a function decorator that is from the unittest mock package
it is used within the scope of the unit test and fixes the value of time.time() 
this allows the test to be called and not raise an error due to 
time.time() being dynamic
"""

