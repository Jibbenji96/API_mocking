from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_catfacts_calls_mock_API_to_provide_cat_fact():
    requester_mock = Mock(name = "requester")
    response_mock = Mock(name = "response")

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "fact":"A cat has the power to sometimes heal themselves by purring. A domestic cat's purr has a frequency of between 25 and 150 Hertz, which happens to be the frequency at which muscles and bones best grow and repair themselves. ",
                                        "length":222
                                        }

    cat_fact = CatFacts(requester_mock)
    assert cat_fact.provide() == "Cat fact: A cat has the power to sometimes heal themselves by purring. A domestic cat's purr has a frequency of between 25 and 150 Hertz, which happens to be the frequency at which muscles and bones best grow and repair themselves. "
