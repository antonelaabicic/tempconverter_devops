def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_student_name(client):
    response = client.get("/")
    assert b"Antonela Abicic" in response.data

def test_college_name(client):
    response = client.get("/")
    assert b"Algebra University College" in response.data