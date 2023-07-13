import json

import allure
from allure import attachment_type


def test_attachments():
    allure.attach('Text content', name='TEXH', attachment_type=attachment_type.TEXT)
    allure.attach('Text content', name='Content text', attachment_type=attachment_type.TEXT)
    allure.attach('<h1>Hello, World!<h1>', name='HTML', attachment_type=attachment_type.TEXT)
    allure.attach(json.dumps({'first': 1, 'second': 2}), name="Json", attachment_type=attachment_type.JSON)