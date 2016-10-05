try:
    import mock
except ImportError:
    from unittest import mock

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture(scope="function")
def driver():
    ''' Returns a mock selenium driver object
    '''
    return mock.create_autospec(webdriver.Firefox)


@pytest.fixture(scope="function")
def element():
    ''' Returns a mock selenium element object
    '''
    return mock.create_autospec(WebElement)
