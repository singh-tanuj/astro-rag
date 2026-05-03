from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "Astro RAG API" in r.json()["message"]

def test_ask():
    payload = {"query": "mars in 11th house"}
    r = client.post("/ask", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["parsed_query"]["planet"] == "Mars"
    assert data["parsed_query"]["house"] == "11"
    assert len(data["sources"]) >= 1