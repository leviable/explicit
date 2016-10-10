try:
    import mock
except ImportError:
    from unittest import mock

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from explicit import waiter

CSS = By.CSS_SELECTOR


def test_find_element_with_defaults(driver, element):
    """ Verify the waiter can find and return an element
    """
    mock_css_path = "div.mock-css-path"

    driver.find_element.side_effect = [None, element]

    elem = waiter.find_element(driver, mock_css_path)

    assert driver.find_element.called
    assert elem is element
    assert len(driver.mock_calls) == 2
    assert driver.find_element.call_args_list == [mock.call(CSS, mock_css_path),
                                                  mock.call(CSS, mock_css_path)]


def test_find_element_with_non_defaults(driver, element):
    """ Verify the waiter can find and return an element when using
        non-default kwargs
    """
    mock_xpath_path = "div[@id=mock-id]"

    driver.find_element.side_effect = [None, element]

    elem = waiter.find_element(driver, mock_xpath_path, by=By.XPATH)

    assert driver.find_element.called
    assert elem is element
    assert len(driver.mock_calls) == 2
    assert driver.find_element.call_args_list == [mock.call(By.XPATH, mock_xpath_path),
                                                  mock.call(By.XPATH, mock_xpath_path)]


def test_find_write_with_defaults(driver, element):
    """ Verify the waiter can find and write to an element, using
        default kwargs
    """
    mock_css_path = "div.mock-css-path"
    mock_write_string = "mock write string"

    driver.find_element.side_effect = [None, element]

    elem = waiter.find_write(driver, mock_css_path, mock_write_string)

    # Element locating asserts
    assert driver.find_element.called
    assert elem is element
    assert len(driver.mock_calls) == 2
    assert driver.find_element.call_args_list == [mock.call(CSS, mock_css_path),
                                                  mock.call(CSS, mock_css_path)]

    # Element writing asserts
    assert elem.clear.called
    assert len(elem.send_keys.call_args_list) == 1
    assert elem.send_keys.call_args == mock.call(mock_write_string)


def test_find_write_with_non_defaults(driver, element):
    """ Verify the waiter can find and write to an element, using
        non-default kwargs
    """
    mock_id_path = "mock id"
    mock_write_string = "mock write string"

    driver.find_element.side_effect = [None, element]

    elem = waiter.find_write(driver, mock_id_path, mock_write_string,
                             by=By.ID, clear_first=False, send_enter=True)

    # Element locating asserts
    assert driver.find_element.called
    assert elem is element
    assert len(driver.mock_calls) == 2
    assert driver.find_element.call_args_list == [mock.call(By.ID, mock_id_path),
                                                  mock.call(By.ID, mock_id_path)]

    # Element writing asserts
    assert not elem.clear.called
    assert len(elem.send_keys.call_args_list) == 2
    assert elem.send_keys.call_args_list == [mock.call(mock_write_string),
                                             mock.call(Keys.ENTER)]
