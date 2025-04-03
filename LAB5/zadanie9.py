from unittest.mock import Mock, call

mock = Mock()

mock.method(1, 2)
mock.method("a", "b")
mock.method(x=1, y=2)

call1 = call.method(1, 2)
call2 = call.method("a", "b")
call3 = call.method(x=1, y=2)

actual_calls = mock.mock_calls
print(f"call1  actual_calls: {call1 in actual_calls}")
print(f"call2  actual_calls: {call2 in actual_calls}")
print(f"call3  actual_calls: {call3 in actual_calls}")

expected_calls = [
    call.method(1, 2),
    call.method("a", "b"),
    call.method(x=1, y=2)
]

is_matching = actual_calls == expected_calls
print(is_matching)

print(f"Type: {type(call1)}")
print(f"String: {str(call1)}")
print(f"Name: {call1[0]}")
print(f"Positional args: {call1[1]}")
print(f"Keyword args: {call1[2]}")

positional_call = call.test_method(1, 2, 3)
named_call = call.test_method(a=1, b=2, c=3)
mixed_call = call.test_method(1, 2, c=3, d=4)

print(positional_call)
print(named_call)
print(mixed_call)