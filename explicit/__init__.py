from selenium.webdriver.common.by import By

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

ID = By.ID
CSS = By.CSS_SELECTOR
XPATH = By.XPATH
