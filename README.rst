explicit
========

|PyPIVersion| |TravisCI| |CoverageStatus| |CodeHealth| |StoriesInReady| |PythonVersions| |Gitter|

Helper class to make working with Selenium explicit waits easier and
more accessible

.. |TravisCI| image:: https://travis-ci.org/levi-rs/explicit.svg?branch=master
    :target: https://travis-ci.org/levi-rs/explicit
.. |CoverageStatus| image:: https://coveralls.io/repos/github/levi-rs/explicit/badge.svg
   :target: https://coveralls.io/github/levi-rs/explicit
.. |CodeHealth| image:: https://landscape.io/github/levi-rs/explicit/master/landscape.svg?style=flat
   :target: https://landscape.io/github/levi-rs/explicit/master
.. |StoriesInReady| image:: https://badge.waffle.io/levi-rs/explicit.svg?label=ready&title=Ready
   :target: http://waffle.io/levi-rs/explicit
.. |PyPIVersion| image:: https://badge.fury.io/py/explicit.svg
    :target: https://badge.fury.io/py/explicit
.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/explicit.svg
    :target: https://wiki.python.org/moin/Python2orPython3
.. |Gitter| image:: https://badges.gitter.im/levi-rs/explicit.svg
    :alt: Join the chat at https://gitter.im/levi-rs/explicit
    :target: https://gitter.im/levi-rs/explicit?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Explicit is designed to minimize or eleminate the common frustrations encountered when using
Selenium on webpages with dynamicly loaded and/or javascript driven content. Typically, a developer
will try to use the webdriver's default ``find_element_by_<XPATH, CSS, ID, LINK TEXT, ETC>`` to
locate an element, only to get hit with various exceptions like NoSuchElementException,
StaleElementReferenceException, and so on.

Selenium includes several tools to address these limitations, most notibly implicit and explicit
waits. While enabling the implicit wait is easy to do, it becomes increasingly problematic as
scripts become more complex. Explicit waits offer a much more powerful alternative, giving the
developer more fine tuned controls, but at the expense of added complexity.

The Explicit package abstracts away the complexities associated with explicit waits by wrapping
commonly used functionality in an easy to use API.

Consider this example:
You want to use Selenium to log into Github from the 404 page. You write a script like this to fill
in the login credentials and click the login button:

.. code-block:: python

    from selenium import webdriver

    driver = webdriver.Chrome()

    try:
        driver.get("https://github.com/this/doesntexist")

        username_field = driver.find_element_by_id("login_field")
        username_field.click()
        username_field.send_keys("my_username")

        password_field = driver.find_element_by_id("password")
        password_field.click()
        password_field.send_keys("my_password")

        login_button = driver.find_element_by_css_selector("input.btn-primary")
        login_button.click()

    finally:
        driver.quit()

When you run the program, however, you get an immediate exception:

::

    (.venv35) ➜  explicit ✗ python example.py
    Traceback (most recent call last):
    File "example.py", line 9, in <module>
        username_field = driver.find_element_by_id("login_field")
    <...>
        raise exception_class(message, screen, stacktrace)
    selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"login_field"}

The reason for the execption, which might not be readily apparent, is that the login modal on that
page loads in after the page loads. When the script runs it attempts to immediately find the field
element after control is returned from the `driver.get` call. Since the element isn't in the DOM
yet, Selenium throws the NoSuchElementException.

|GithubLogin|

.. |GithubLogin| image:: http://i.imgur.com/T3gnnhU.gif
    :target: https://github.com/this/doesntexist

Explicit easily solves this by waiting for the element to load in:

.. code-block:: python

    from explicit import waiter
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()

    try:
        driver.get("https://github.com/this/doesntexist")

        username_field = waiter.find_element(driver, "login_field", By.ID)
        username_field.click()
        username_field.send_keys("my_username")

        password_field = waiter.find_element(driver, "password", By.ID)
        password_field.click()
        password_field.send_keys("my_password")

        login_button = waiter.find_element(driver, "input.btn-primary", By.CSS_SELECTOR)
        login_button.click()
    finally:
        driver.quit()

Additionally, you can use explicit to handle the writing:

.. code-block:: python

    from explicit import waiter
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()

    try:
        driver.get("https://github.com/this/doesntexist")

        waiter.find_write(driver, "login_field", "my_username", by=By.ID)

        waiter.find_write(driver, "password", "my_password", by=By.ID, send_enter=True)

    finally:
        driver.quit()
