try:
    import mock
except ImportError:
    from unittest import mock

from selenium.webdriver.common.keys import Keys

from explicit import waiter, CSS, ID, XPATH


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

    elem = waiter.find_element(driver, mock_xpath_path, by=XPATH)

    assert driver.find_element.called
    assert elem is element
    assert len(driver.mock_calls) == 2
    assert driver.find_element.call_args_list == [mock.call(XPATH, mock_xpath_path),
                                                  mock.call(XPATH, mock_xpath_path)]


def test_find_elements_with_defaults(driver, element):
    """ Verify the waiter can find and return all elements
    """
    mock_css_path = "div.mock-css-path"

    driver.find_elements.side_effect = [None, [element, element]]

    elem_list = waiter.find_elements(driver, mock_css_path)

    assert driver.find_elements.called
    assert isinstance(elem_list, list)
    assert all(map(lambda x: x is element, elem_list))
    assert len(driver.mock_calls) == 2
    assert driver.find_elements.call_args_list == [mock.call(CSS, mock_css_path),
                                                   mock.call(CSS, mock_css_path)]


def test_find_elements_with_non_defaults(driver, element):
    """ Verify the waiter can find and return all elements when using
        non-default kwargs
    """
    mock_xpath_path = "div[@id=mock-id]"

    driver.find_elements.side_effect = [None, [element, element]]

    elem_list = waiter.find_elements(driver, mock_xpath_path, by=XPATH)

    assert driver.find_elements.called
    assert isinstance(elem_list, list)
    assert all(map(lambda x: x is element, elem_list))
    assert len(driver.mock_calls) == 2
    assert driver.find_elements.call_args_list == [mock.call(XPATH, mock_xpath_path),
                                                   mock.call(XPATH, mock_xpath_path)]


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
                             by=ID, clear_first=False, send_enter=True)

    # Element locating asserts
    assert driver.find_element.called
    assert elem is element
    assert len(driver.mock_calls) == 2
    assert driver.find_element.call_args_list == [mock.call(ID, mock_id_path),
                                                  mock.call(ID, mock_id_path)]

    # Element writing asserts
    assert not elem.clear.called
    assert len(elem.send_keys.call_args_list) == 2
    assert elem.send_keys.call_args_list == [mock.call(mock_write_string),
                                             mock.call(Keys.ENTER)]


def test_find_one_with_defaults(driver, element):
    """ Verify the waiter can locate one of several possible elements """
    side_effects = [[], [], [element, ], []]
    driver.find_elements_by_css_selector.side_effect = side_effects

    div1 = 'div.mock_1'
    div2 = 'div.mock_2'

    locators = [div1, div2]
    elem = waiter.find_one(driver, locators)

    assert elem is element
    assert driver.method_calls == [mock.call.find_elements_by_css_selector(div1),
                                   mock.call.find_elements_by_css_selector(div2),
                                   mock.call.find_elements_by_css_selector(div1),
                                   mock.call.find_elements_by_css_selector(div2)]


def test_find_one_with_non_defaults(driver, element):
    """ Verify the waiter can locate one of several possible elements,
        using non-default function parameters
    """
    side_effects = [[], [], [element, ], []]
    driver.find_elements_by_id.side_effect = side_effects

    id_1 = 'mock_1'
    id_2 = 'mock_2'

    locators = [id_1, id_2]
    elem = waiter.find_one(driver, locators, elem_type=ID, timeout=20)

    assert elem is element
    assert driver.method_calls == [mock.call.find_elements_by_id(id_1),
                                   mock.call.find_elements_by_id(id_2),
                                   mock.call.find_elements_by_id(id_1),
                                   mock.call.find_elements_by_id(id_2)]
