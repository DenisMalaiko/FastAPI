# ------------- Auth Users -------------
def test_users_requires_auth(client):
    r = client.get(
        "/api/v1/users/"
    )
    assert r.status_code == 401
    assert r.json()["detail"] == "Missing token"

def test_users_requires_token(client):
    r = client.get(
        "/api/v1/users/",
        headers={"Authorization": "Bearer test"},
    )
    assert r.status_code == 401
    assert r.json()["detail"] == "Invalid token"


# ------------- Get Users -------------
def test_users_e2e(client):
    r = client.get(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
    )
    assert r.status_code == 200


# ------------- Creating Users -------------
def test_user_creating_with_missed_field(client):
    r = client.post(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
        json={"name": "John Doe"},
    )
    assert r.status_code == 422
    assert r.json()["detail"][0]["msg"] == "Field required"

def test_user_creating_with_wrong_field_type(client):
    r = client.post(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
        json={"name": 12345, "email": 12345},
    )
    assert r.status_code == 422

    details = r.json()["detail"]
    error_types = {err["loc"][-1]: err["type"] for err in details}

    assert error_types["name"] == "string_type"
    assert error_types["email"] == "string_type"

def test_user_creating_with_redundant_field(client):
    r = client.post(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
        json={"name": "John", "email": "malaiko.denis2@gmail.com", "age": 30},
    )

    assert r.status_code == 422
    assert r.json()["detail"][0]["msg"] == "Extra inputs are not permitted"

def test_user_creating_properly(client):
    r = client.post(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
        json={"name": "John", "email": "malaiko.denis@gmail.com"},
    )

    assert r.status_code == 200

    user_id = r.json()["id"]

    client.delete(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": "Bearer secret"},
    )

def test_exists_user_creating(client):
    email = "duplicate@mail.com"

    first = client.post(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
        json={"name": "John", "email": email},
    )
    assert first.status_code == 200

    second = client.post(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
        json={"name": "John", "email": email},
    )

    assert second.status_code == 400
    assert second.json()["detail"] == "Email already exists"

    user_id = first.json()["id"]

    client.delete(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": "Bearer secret"},
    )


# ------------- Get User By ID -------------
def test_get_user_by_id(client):
    create = client.post(
        "/api/v1/users/",
        headers={"Authorization": "Bearer secret"},
        json={
            "email": "test_user@mail.com",
            "name": "Test User",
        },
    )

    assert create.status_code == 200
    user_id = create.json()["id"]

    try:
        r = client.get(
            f"/api/v1/users/{user_id}",
            headers={"Authorization": "Bearer secret"},
        )

        assert r.status_code == 200
        assert r.json()["id"] == user_id
    finally:
        client.delete(
            f"/api/v1/users/{user_id}",
            headers={"Authorization": "Bearer secret"},
        )


