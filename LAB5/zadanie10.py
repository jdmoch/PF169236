import unittest
from unittest.mock import Mock

class DataService:
    def __init__(self, api_client):
        self.api_client = api_client
        self.max_retries = 3

    def fetch_user_data(self, user_id, details=False):
        retry_count = 0
        while retry_count <= self.max_retries:
            try:
                return self.api_client.get_data(user_id=user_id, details=details)
            except ConnectionError:
                retry_count += 1
                if retry_count > self.max_retries:
                    raise
        return None


class TestDataService(unittest.TestCase):
    def test_fetch_user_data(self):
        api_mock = Mock()

        api_mock.get_data.side_effect = [
            {'name': 'Jan'},
            {'name': 'Anna'}
        ]

        service = DataService(api_mock)

        result1 = service.fetch_user_data(123, details=True)
        result2 = service.fetch_user_data(456, details=True)

        self.assertEqual(result1, {'name': 'Jan'})
        self.assertEqual(result2, {'name': 'Anna'})

        api_mock.get_data.assert_called_with(user_id=456, details=True)

        self.assertEqual(api_mock.get_data.call_count, 2)

        calls = api_mock.get_data.call_args_list
        self.assertEqual(calls[0][1]['user_id'], 123)
        self.assertEqual(calls[1][1]['user_id'], 456)

    def test_retry_mechanism(self):
        api_mock = Mock()

        api_mock.get_data.side_effect = [
            {'data': 'value1'},
            {'data': 'value2'},
            ConnectionError(),
            {'data': 'value4'}
        ]

        service = DataService(api_mock)

        result1 = service.fetch_user_data(1)
        result2 = service.fetch_user_data(2)

        result3 = service.fetch_user_data(3)

        self.assertEqual(result1, {'data': 'value1'})
        self.assertEqual(result2, {'data': 'value2'})
        self.assertEqual(result3, {'data': 'value4'})

        self.assertEqual(api_mock.get_data.call_count, 4)


if __name__ == '__main__':
    unittest.main()