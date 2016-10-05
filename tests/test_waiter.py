from explicit import waiter


def test_find_element(driver, element):
    """ Verify the water can find and return an element
    """
    driver.find_element.side_effect = [None, element]

    elem = waiter.find_element(driver, "div.mock-css-path")

    assert driver.find_element.called
    assert len(driver.mock_calls) == 2
    assert elem is element
