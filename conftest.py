import pytest
from fixture.application import Application

# глобальная переменная для хранения фикстуры
fixture = None

# инициализатор фикстуры
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture =Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture

# фикстура выполнится несмотря на то, что нигде не указана
# благодаря параметру autouse
@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture