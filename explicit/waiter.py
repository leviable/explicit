# -*- coding: utf-8 -*-
"""explicit.waiter

A collection of helper functions to make working with Selenium's
explicit wait functionality easier.

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 30
""" int: Default timeout value, in seconds"""

CSS = By.CSS_SELECTOR
""" By: Default Selenium search type (CSS Selector)"""


def find_element(driver, elem_path, by=CSS, timeout=TIMEOUT, poll_frequency=0.5):
    """ Find and return an element once located

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


def find_elements(driver, elem_path, by=CSS, timeout=TIMEOUT, poll_frequency=0.5):
    """ Find and return all elements once located

    find_elements locates all elements on the page, waiting
    for up to timeout seconds. The elements, when located,
    are returned. If not located, a TimeoutException is raised.

    Args:
        driver (selenium webdriver or element): A driver or element
        elem_path (str): String used to located the element
        by (selenium By): Selenium By reference
        timeout (int): Selenium Wait timeout, in seconds
        poll_frequency (float): Selenium Wait polling frequency, in seconds

    Returns:
        list of elements: Selenium element

    Raises:
        TimeoutException: Raised when target element isn't located
    """
    wait = WebDriverWait(driver, timeout, poll_frequency)
    return wait.until(EC.presence_of_all_elements_located((by, elem_path)))


def find_write(driver, elem_path, write_str, clear_first=True, send_enter=False,
               by=CSS, timeout=TIMEOUT, poll_frequency=0.5):
    """ Find a writable element and write to it

    find_write locates a writable element on the page, waiting
    for up to timeout seconds. Once found, it writes the string
    to it.

    Args:
        driver (selenium webdriver or element): A driver or element
        elem_path (str): String used to located the element
        write_str (str): String to write
        clear_first (bool): Clear the contents before writing (default True)
        send_enter (bool): Send a keyboard ENTER after writing string
        by (selenium By): Selenium By reference
        timeout (int): Selenium Wait timeout, in seconds
        poll_frequency (float): Selenium Wait polling frequency, in seconds

    Returns:
        element: Selenium element

    Raises:
        TimeoutException: Raised when target element isn't located
    """
    elem = find_element(driver, elem_path=elem_path, by=by, timeout=timeout,
                        poll_frequency=poll_frequency)

    if clear_first:
        elem.clear()

    elem.send_keys(write_str)

    if send_enter:
        elem.send_keys(Keys.ENTER)

    return elem
