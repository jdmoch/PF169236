from unittest.mock import Mock

mock = Mock()
mock.method1(4)
mock.method2('aaa')
mock.nested.method(32)

print("before:")
print("method1:", mock.method1.call_count)
print("mock_calls:", mock.mock_calls)

mock.reset_mock()
print("\n after:")
print("method1", mock.method1.call_count)
print("mock_calls:", mock.mock_calls)

mock.method1.return_value = 42
mock.reset_mock(return_value=False)
print("\nPo resecie")
print("method1 return_value:", mock.method1.return_value)