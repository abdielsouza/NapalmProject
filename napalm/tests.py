import pytest
from napalm.napalm import Napalm

@pytest.fixture
def application():
    return Napalm()

@pytest.fixture
def client(application):
    return application.test_session()


def test_napalm_test_client_can_send_requests(application, client):
    RESPONSE_TEXT = "THIS IS COOL"

    @application.route("/hey")
    def cool(req, resp):
        resp.text = RESPONSE_TEXT

    assert client.get("http://testserver/hey").text == RESPONSE_TEXT

def test_parameterized_route(application, client):
    @application.route("/{name}")
    def hello(req, resp, name):
        resp.text = f"hey {name}"

    assert client.get("http://testserver/matthew").text == "hey matthew"
    assert client.get("http://testserver/ashley").text == "hey ashley"

def test_default_404_response(client):
    response = client.get("http://testserver/doesnotexist")

    assert response.status_code == 404
    assert response.text == "Not found."