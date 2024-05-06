import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
from selenium.common import WebDriverException


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""
    code = None
    log_entries = driver.get_log("performance")
    for entry in log_entries:
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    get_taxi_button = (By.XPATH, ".//button[text()='Pedir un taxi']")
    comfort_tariff_button = (By.XPATH, '//img[@alt="Comfort"]')
    add_new_phone_number_button = (By.XPATH, "/html/body/div/div/div[3]/div[3]/div[1]/div[3]/div[1]/button")
    phone_number_field = (By.ID, "phone")
    phone_code_field = (By.XPATH, "//*[@id='code']")
    confirm_code_phone_button = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")
    next_window_phone_number = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    close_phone_number_window = (By.CSS_SELECTOR, ".number-picker > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)")
    payment_method_button = (By.CLASS_NAME, "pp-text")
    create_new_credit_card_button = (By.CLASS_NAME, "pp-plus")
    credit_card_number_field = (By.ID,"number")
    credit_card_code_field = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    add_credit_card = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/form/div[3]/button[1]]")
    close_payment_method_window = (By.CSS_SELECTOR, ".payment-picker > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)")
    comments_field = (By.ID, "comment")
    add_blanket_and_scarves_switch = (By.CSS_SELECTOR, "div.r-type-switch:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)")
    add_ice_cream_button = (By.CSS_SELECTOR, "div.sub:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3)")
    ice_cream_counter = (By.CSS_SELECTOR, "div.sub:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
    book_taxi_button = (By.CLASS_NAME, 'smart-button')
    waiting_counter = (By.CLASS_NAME, "order-header-time")
    book_details_button = (By.CSS_SELECTOR, 'div.order-btn-group:nth-child(3) > button:nth-child(1)')



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_taxi(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        return self.driver.find_element(*self.get_taxi_button).click()

    def comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        return self.driver.find_element(*self.comfort_tariff_button).click()


    def add_new_phone_number(self,phone_number):

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.add_new_phone_number_button))
        self.driver.find_element(*self.add_new_phone_number_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)
        self.driver.find_element(*self.next_window_phone_number).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.phone_code_field))
        self.driver.find_element(*self.phone_code_field).send_keys(retrieve_phone_code(self.driver))
        time.sleep(4)
        self.driver.find_element(*self.confirm_code_phone_button).click()


    def get_phone_number_field_value(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')


    def add_new_credit_card(self,credit_card_number,credit_card_code):
        self.driver.find_element(*self.payment_method_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.create_new_credit_card_button))
        self.driver.find_element(*self.create_new_credit_card_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.credit_card_number_field))
        self.driver.find_element(*self.credit_card_number_field).clear()
        self.driver.find_element(*self.credit_card_number_field).send_keys(credit_card_number)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.credit_card_code_field))
        self.driver.find_element(*self.credit_card_code_field).clear()
        self.driver.find_element(*self.credit_card_code_field).send_keys(credit_card_code)
        self.driver.find_element(*self.credit_card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*self.add_credit_card).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.close_payment_method_window))
        self.driver.find_element(*self.close_payment_method_window).click()

    def add_comment(self,comment):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comments_field))
        self.driver.find_element(*self.comments_field).send_keys(comment)

    def get_comment(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comments_field))
        return self.driver.find_element(*self.comments_field).get_property('value')

    def add_blanket_and_scarves(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.add_blanket_and_scarves_switch))
        element = self.driver.find_element(*self.add_blanket_and_scarves_switch)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def add_ice_cream(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.add_ice_cream_button))
        self.driver.find_element(*self.add_ice_cream_button).click()
        self.driver.find_element(*self.add_ice_cream_button).click()



    def book_taxi(self):
        self.driver.find_element(*self.book_taxi_button).click()

    def wait_driver_information(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.waiting_counter))
        element = self.driver.find_element(*self.waiting_counter)
        WebDriverWait(self.driver, 60).until(lambda driver: element.text == "00:01")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.book_details_button))
        self.driver.find_element(*self.book_details_button).click()

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # !!!!!!   Modifique el codigo debido a que la opcion desired capabilities ya no es compatible con la version de selenium actual   !!!!!!!1
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
        chrome_options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=chrome_options)

    """
    La prueba test_set_route comrpueba la funcionalidad de los campos para introducir las direccones "Desde" y "Hasta"
    """
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.get_taxi()

    """
    La prueba test_select_comfort_tariff comprueba la funcionalidad de poder seleccionar la tarifa Comfort
    """
    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.test_set_route()
        routes_page.comfort_tariff()

    """
    La prueba test_fill_new_phone_number comprueba la funcionalidad de agregar un numero de telefono cuando se escoge la tarifa Comfort
    """
    def test_fill_new_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        self.test_select_comfort_tariff()
        routes_page.add_new_phone_number(phone_number)
        assert routes_page.get_phone_number_field_value() == phone_number

    """
    La prueba test_add_comment comprueba la funcionalidad de agregar una nueva tarjeta de credito cuando se escoge la tarifa Comfort
    """
    def test_fill_new_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        self.test_select_comfort_tariff()
        routes_page.add_new_credit_card(card_number,card_code)

    """
    La prueba test_add_comment comprueba la funcionalidad de agregar comentarios al conductor cuando se escoge la tarifa Comfort
    """
    def test_add_comment(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.test_fill_new_credit_card()
        comment = "Comentario"
        routes_page.add_comment(comment)
        assert routes_page.get_comment() == comment

    """
    La prueba test_add_blanket_and_scarves comprueba la funcionalidad de agregar mantas y pañuelos cuando se escoge la tarifa Comfort
    """

    def test_add_blanket_and_scarves(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.test_add_comment()
        routes_page.add_blanket_and_scarves()

    """
    La prueba test_add_chocolate_ice_cream comprueba la funcionalidad de agregar dos helados de chocolate cuando se escoge la tarifa Comfort
    """

    def test_add_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.test_add_blanket_and_scarves()
        routes_page.add_ice_cream()

    """
    La prueba test_view_modal_find_taxi comprueba la funcionalidad de el boton para pedir eñ taxi una vez los campos necesarios se llenen de manera correcta
    """
    def test_view_modal_find_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.test_add_comment()
        routes_page.book_taxi()


    """
    La prueba test_view_driver_information lleva a cabo la validancion de todo el proceso y al final hace una espera para ver la informacion del conductor
    """

    def test_view_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.test_add_comment()
        routes_page.wait_driver_information()




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
