from app import app, Temperature

def test_temperature_record_is_created(client):
    with app.app_context():
        before = Temperature.query.count()

    response = client.post("/", data={"celsius": "25"}, follow_redirects=True)

    with app.app_context():
        after = Temperature.query.count()

    assert response.status_code == 200
    assert after == before + 1

def test_temperature_values_are_saved_correctly(client):
    client.post("/", data={"celsius": "30"}, follow_redirects=True)

    with app.app_context():
        latest = Temperature.query.order_by(Temperature.id.desc()).first()

    assert latest is not None
    assert latest.celsius == 30
    assert latest.fahrenheit == 86.0