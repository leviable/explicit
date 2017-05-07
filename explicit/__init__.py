from pbr.version import VersionInfo
from selenium.webdriver.common.by import By

__version__ = VersionInfo('explicit').semantic_version().release_string()

CLASS_NAME = By.CLASS_NAME
CSS = By.CSS_SELECTOR
ID = By.ID
LINK = By.LINK_TEXT
NAME = By.NAME
PARTIAL_LINK = By.PARTIAL_LINK_TEXT
TAG = By.TAG_NAME
XPATH = By.XPATH
