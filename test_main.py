import pytest
from fastapi.testclient import TestClient
from main import app
from main import supabase
from datetime import datetime, timedelta
from main import generate_locker_id
from main import BaseModel

client = TestClient(app)

def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_generate_locker_id():
    locker_id = generate_locker_id()
    assert len(locker_id) == 5
    assert locker_id.isalnum()

def test_datetime():
    current_time = datetime.now()
    past_time = current_time - timedelta(minutes=1)
    future_time = current_time + timedelta(minutes=1)
    assert current_time > past_time
    assert current_time < future_time
