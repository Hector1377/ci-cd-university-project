from httpx import AsyncClient
from main import app

def test_root():
    assert "CI/CD Python Project" in str(app)

def test_health():
    assert "healthy" in str(app)
