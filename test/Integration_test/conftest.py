import pytest
from fastapi.testclient import TestClient
from app.main import create_application

@pytest.fixture(scope = 'function')
def testing_app():
      app = create_application()
      test_app = TestClient(app)
      return test_app


    


