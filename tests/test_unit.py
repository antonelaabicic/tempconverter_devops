def test_home_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_student_name_is_displayed(client):
    response = client.get("/")
    assert b"Antonela Abicic" in response.data

def test_college_name_is_displayed(client):
    response = client.get("/")
    assert b"Algebra University College" in response.data