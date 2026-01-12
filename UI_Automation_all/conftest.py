import pytest

@pytest.fixture()
def set_teardown():
    print('before tc')
    yield
    print('after tc')