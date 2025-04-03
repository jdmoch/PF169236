from unittest.mock import Mock

mock = Mock()

mock.method.side_effect = lambda x: f"Result{x}" if isinstance(x, str) else x * 2

print(mock.method("test"))
print(mock.method(5))

mock.another_method.return_value = "default"
mock.another_method.side_effect = lambda: "side effect"

print(mock.another_method())

# Create nested mocks
mock.nested.deeply.method.return_value = "nested"
print(mock.nested.deeply.method())


mock.db.connect.return_value = "connected"
mock.db.query.return_value = ["row1", "row2"]
print(mock.db.connect())
print(mock.db.query())

mock.configure_mock(
    name="configured_mock",
    api_key="12345",
    settings={"timeout": 30, "retry": True}
)

print(mock.name)
print(mock.api_key)
print(mock.settings)