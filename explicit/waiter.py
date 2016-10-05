# -*- coding: utf-8 -*-
"""explicit.waiter

A collection of helper functions to make working with Selenium's
explicit wait functionality easier.

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 30
""" int: Default timeout value, in seconds"""

CSS = By.CSS_SELECTOR
""" By: Default Selenium search type (CSS Selector)"""


def find_element(driver, elem_path, by=CSS, timeout=TIMEOUT, poll_frequency=0.5):
    """ find and return an element once located

    find_element locates an element on the page, waiting
    for up to timeout seconds. The element, when located,
    is returned. If not located, a TimeoutException is raised.

    Args:
        driver (selenium webdriver or element): A driver or element
        elem_path (str): String used to located the element
        by (selenium By): Selenium By reference
        timeout (int): Selenium Wait timeout, in seconds
        poll_frequency (float): Selenium Wait polling frequency, in seconds

    Returns:
        element: Selenium element

    Raises:
        TimeoutException: Raised when target element isn't located
    """
    wait = WebDriverWait(driver, timeout, poll_frequency)
    return wait.until(EC.presence_of_element_located((by, elem_path)))
