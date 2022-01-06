import os

from selenium import webdriver

import booking.constants as const
from booking.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    

    def __init__(self,  driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()


    def __enter__(self):
        print('The bot is running...')
        return self


    def __exit__(self, exc_type, exc_value, trace):
        # Mientras teardown sea True el navegador seguira abierto
        # incluso despues de su ejecucion
        if self.teardown:
            self.quit()
            print('Exiting...')


    def land_first_page(self):
        # Ejecutamos la url del sitio a aplicar el bot
        self.get(const.BASE_URL)


    def change_currency(self, currency=None):
        # Buscamos el boton para abrir el menu el cambio de moneda
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Elegir tu moneda"]'
        )
        currency_element.click()

        # Buscamos el boton del tipo de cambio a aplicar
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()


    def select_place_to_go(self, place_to_go):
        # Busca la caja del input
        search_field = self.find_element_by_id('ss')
        # Limpia cualquier dato que haya en el
        search_field.clear()
        # Le envia nuestro lugar de destino
        search_field.send_keys(place_to_go)

        # Busca el primer resultado
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()


    def select_dates(self, check_in_date, check_out_date):

        # Definimos la fecha de llegada
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        # Definimos la fecha de vuelta 
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_in_element.click()
    
    def select_adults(self, count=1):
        # Busca la caja donde se encuentra el numero de personas 
        # y habitaciones
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            # Busca el boton que disminuye el numero de personas adultas
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Reduce el número de Adultos"]'
            )
            decrease_adults_element.click()

            # Buscamos el input con el numero de adultos
            adults_value_element = self.find_element_by_id('group_adults')
            # Detectamos el valor del input(numero de adultos)
            adults_value = adults_value_element.get_attribute(
                'value'
            ) 
            # El while loop iterara hasta que el numero de adultos 
            # llege a 1, si es asi abandonamos el while loop
            if int(adults_value) == 1:
                break # Ahora el numero de adultos se configurara a 1


        # Busca el boton que aumenta el numero de personas adultas
        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Aumenta el número de Adultos"]'
        )

        # En el for loop le indicamos para cuantos cuantos adultos 
        # sera la reserva. Ojo que el while loop anterior configuramos 
        # por defecto el numero de adultos a 1 
        for _ in range(count - 1):
            # Por cada adulto extra hara click en aumentar adulto 
            increase_button_element.click()
            
    def click_search(self):
        # Buscamos el boton "buscar" para realizar la busqueda
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)
        filtration.sort_price_lowest_first()
