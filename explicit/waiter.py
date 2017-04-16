# -*- coding: utf-8 -*-
"""explicit.waiter

A collection of helper functions to make working with Selenium's
explicit wait functionality easier.

"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from explicit import (
    CLASS_NAME, CSS, ID, LINK, NAME, PARTIAL_LINK, TAG, XPATH)

TIMEOUT = 30
""" int: Default timeout value, in seconds"""


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


def find_one(driver, locator_list, elem_type=CSS, timeout=TIMEOUT):
    """
    Args:
        driver (selenium webdriver): Selenium webdriver object
        locator_list (:obj: `list` of :obj: `str`): List of CSS selector strings
        elem_type (Selenium By types): Selenium By type (i.e. By.CSS_SELECTOR)
        timeout (int): Number of seconds to wait before timing out

    Returns:
        Selenium Element

    Raises:
        TimeoutException: Raised if no elements are found within the TIMEOUT
    """
    def _find_one(driver):
        """ Expected Condition to find and return first located element """
        finders = {
            CLASS_NAME: driver.find_elements_by_class_name,
            CSS: driver.find_elements_by_css_selector,
            ID: driver.find_elements_by_id,
            LINK: driver.find_elements_by_link_text,
            NAME: driver.find_elements_by_name,
            PARTIAL_LINK: driver.find_elements_by_partial_link_text,
            TAG: driver.find_elements_by_tag_name,
            XPATH: driver.find_elements_by_xpath
        }

        elems = [finders[elem_type](loc) for loc in locator_list]

        if any([len(elem_list) > 0 for elem_list in elems]):
            return elems
        else:
            return False

    raw_results = WebDriverWait(driver, timeout).until(_find_one)

    # Pull out any found elements from lists
    results = [elem for elem_list in raw_results for elem in elem_list]

    return results.pop() if len(results) == 1 else results


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
