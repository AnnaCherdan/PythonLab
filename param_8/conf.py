import pytest


@pytest.fixture(scope='function', params=[
    ('abcdefg', 'abcdefg?'),
    ('abc', 'abc!'),
    ('abcde', 'abcde.')
])
def param_test(request):
    return request.param
