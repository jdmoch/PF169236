from unittest.mock import Mock

mock = Mock(name="my_mock")

mock.get_data.return_value = 'test_test'

result = mock.get_data('user')

mock.get_data.assert_called_with('user')

print(mock.get_data.call_args)