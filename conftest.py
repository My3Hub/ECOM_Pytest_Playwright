import pytest
from requests import session


@pytest.fixture(scope="session")
def user_details(request):
    return request.param