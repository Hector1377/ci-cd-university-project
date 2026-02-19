from main import app

def test_app_title():
    assert app.title == "CI/CD Python Project"

def test_health_endpoint_exists():
    routes = [route.path for route in app.routes]
    assert "/health" in routes
