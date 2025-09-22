from selenium.webdriver.common.by import By
import time
from pages.elements_page import Elementspage

def test_navigate_to_elements_page(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert "elements" in driver.current_url

def test_locate_by_id(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_id_visible()
    assert elements_page.get_menu_check_box_id_text() == "Text Box"

def test_locate_by_css_selector(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_css_visible()

def test_locate_by_xpath(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_xpath_visible()