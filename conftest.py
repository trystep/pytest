import pytest
from pages.application import Application
import json
import os

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    with open(os.path.join(os.path.dirname(__file__), 'config.json')) as config_file:
        config = json.load(config_file)
    if fixture is None:
        fixture = Application(base_url=config['baseUrl'])
        fixture.session.login(username=config["username"], password=config["password"])
    request.addfinalizer(fixture.destroy)
    return fixture
