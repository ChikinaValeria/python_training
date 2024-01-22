import pytest
from fixture.application import Application

# инициализатор фикстуры
@pytest.fixture
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destroy)
    return fixture