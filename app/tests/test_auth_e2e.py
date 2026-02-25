def test_smoke(client):
    r = client.get("/")
    assert r.status_code == 200


def test_me_requires_auth(client):
    r = client.get("/me")
    assert r.status_code == 401
    assert r.json()["detail"] == "Missing token"

def test_me_with_test_token(client):
    r = client.get(
        "/me",
        headers={"Authorization": "Bearer TEST TOKEN"},
    )
    assert r.status_code == 401
    assert r.json()["detail"] == "Invalid token"

def test_me_with_valid_token(client):
    r = client.get(
        "/me",
        headers={"Authorization": "Bearer secret"},
    )
    assert r.status_code == 200
    assert r.json()["role"] == "user"