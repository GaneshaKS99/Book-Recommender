from django.test import TestCase

# Create your tests here.
def testing():
    response = app.test_client().get('http://127.0.0.1:8000/')
    assert response.status_code == 200
    print(" page test done")
