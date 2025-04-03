from unittest.mock import Mock, call

mock = Mock()
mock.method1('aaa')
mock.method1('bbb')
mock.method2()

mock.method1.assert_called()
mock.method2.assert_called_once()
mock.method_not_called = Mock()
mock.method_not_called.assert_not_called()

mock.method1.assert_called_with('bbb')
mock.method1.assert_any_call('aaa')

expected_calls = [
    call('aaa'),
    call('bbb')
]
mock.method1.assert_has_calls(expected_calls)
mock.method1.assert_has_calls(expected_calls, any_order=True)

print("mock:", mock.mock_calls)
print("method:", mock.method1.mock_calls)