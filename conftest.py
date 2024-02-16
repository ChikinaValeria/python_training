import pytest
import json
import os.path
from fixture.application import Application

# глобальная переменная для хранения фикстуры
fixture = None
target = None

# инициализатор фикстуры
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        # путь к текущему файлу
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture =Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

# фикстура выполнится несмотря на то, что нигде не указана
# благодаря параметру autouse
@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    #parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")
