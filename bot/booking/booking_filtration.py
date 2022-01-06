# Este archivo incluira una clase con una instancia con metodos
# Que sera responsable para interactuar con nuestro website
# Después nosotros tendremos algunos resultados, para aplicar algunas filtraciones
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
            )
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
    
        for star_value in star_values:
            for star_child_element in star_child_elements:
                if str(star_child_element.get_attribute('innerHTML')).strip() == f'{star_value} estrellas':
                    star_child_element.click()
    
    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        action = ActionChains(self.driver)
        action.double_click(element).perform()
