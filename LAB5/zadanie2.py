from unittest.mock import Mock

class SampleClass:
    def sample_method(self, arg):
        pass

real_object = SampleClass()
mock = Mock(spec=real_object, autospec=True)

mock.sample_method.side_effect = [
    "1",
    "2",
    "3"
]

print(mock.sample_method("arg1"))
print(mock.sample_method("arg2"))
print(mock.sample_method("arg3"))

def modify_args(arg):
    return arg

mock.sample_method.side_effect = modify_args
print(mock.sample_method("test_arg"))

mock.sample_method.side_effect = ValueError("Test exception")
