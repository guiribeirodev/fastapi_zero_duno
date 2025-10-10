from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World'}  # Assert


def test_hellohtml_deve_retornar_ok_e_html():
    client = TestClient(app)  # Arrange

    response = client.get('/hellohtml')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert '<h1>Hello, HTML!</h1>' in response.text  # Assert
