from selenium.webdriver.common.by import By

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

CLASS_NAME = By.CLASS_NAME
CSS = By.CSS_SELECTOR
ID = By.ID
LINK = By.LINK_TEXT
NAME = By.NAME
PARTIAL_LINK = By.PARTIAL_LINK_TEXT
TAG = By.TAG_NAME
XPATH = By.XPATH
