
import flask
import pytest

import main


# Create a fake "app" for generating test request contexts.
@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)


class TestItems(object):

    def test_get_item(self, app):
        with app.test_request_context(path='item/8y3WApnnmudDJlnddE9X'):
            response = main.item(flask.request)
            assert response['name'] == 'fruit'

    def test_post_item(self, app):
        payload = {
            'name': 'vegetable',
            'attribute1': 'carrot'
        }
        with app.test_request_context(json=payload, method='POST'):
            main.item(flask.request)
        with app.test_request_context(path='item/vegetable'):
            response = main.item(flask.request)
            assert response['attribute1'] == 'carrot'

