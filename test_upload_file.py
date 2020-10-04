from fastapi.testclient import TestClient

# TODO FIX
from server import app

client = TestClient(app)

def test_entry():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_download():
    response = client.post(
        "/downloads",
        headers={'Content-Type': 'application/json' },
        json={"url": "https://www.youtube.com/watch?v=cTmZ6vvdvkM"}
    )

    assert response.status_code == 200
    assert response.headers.get("content-type")  == "video/mp4"
