import pytest
from ..app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_root_route(client):
    response = client.get("/")
    assert response.status_code == 200

def test_roster_route_no_data(client):
    resp = client.get("/roster")
    assert resp.status_code == 200

def test_roster_route_post(client):
    resp = client.post("/roster", data = {"team_name" : "yankees"})
    assert resp.is_json
    json_data = resp.get_json()
    assert "Pitchers" in json_data

def test_roster_data(client):
    resp = client.post("/roster", data = {"team_name" : "cubs"})
    assert resp.is_json
    data = resp.get_json()
    assert "Catchers" in data

def test_roster_division_1(client):
    resp = client.post("/roster", data = {"team_name" : "redsox"})
    assert resp.is_json
    assert "Catchers" in resp.get_json()

def test_roster_division_2(client):
    resp = client.post("/roster" ,data = {"team_name" : "braves"})
    assert resp.is_json
    assert "Catchers" in resp.get_json()