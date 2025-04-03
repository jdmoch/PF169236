from unittest.mock import Mock, ANY

mock = Mock()
mock.complex_method(10, "test", user={"name": "John", "id": 123}, options=[1, 2, 3])
mock.complex_method.assert_called_with(10, ANY, user=ANY, options=ANY)
mock.complex_method.assert_called_with(10, ANY, user={"name": "John", "id": 123}, options=ANY)

mock.data_types_method(42, "string", [1, 2, 3], {"a": 1})
mock.data_types_method.assert_called_with(ANY, ANY, ANY, ANY)

class ValidateType:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        return isinstance(other, self.expected_type)

mock.typed_method(42, "string", [1, 2, 3])
mock.typed_method.assert_called_with(
    ValidateType(int),
    ValidateType(str),
    ValidateType(list)
)
print("Sukces")