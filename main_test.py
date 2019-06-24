# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

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

