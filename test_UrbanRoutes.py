import data
from selenium import webdriver
import pages
class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--log-level=0')
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    """
    La prueba test_set_route comrpueba la funcionalidad de los campos para introducir las direccones "Desde" y "Hasta"
    """
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.get_taxi()

    """
    La prueba test_select_comfort_tariff comprueba la funcionalidad de poder seleccionar la tarifa Comfort
    """
    def test_select_comfort_tariff(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.comfort_tariff()

    """
    La prueba test_fill_new_phone_number comprueba la funcionalidad de agregar un numero de telefono cuando se escoge la tarifa Comfort
    """
    def test_fill_new_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        phone_number = data.PHONE_NUMBER
        routes_page.add_new_phone_number(phone_number)
        assert routes_page.get_phone_number_field_value() == phone_number

    """
    La prueba test_add_comment comprueba la funcionalidad de agregar una nueva tarjeta de credito cuando se escoge la tarifa Comfort
    """
    def test_fill_new_credit_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        card_number = data.CARD_NUMBER
        card_code = data.CARD_CODE
        routes_page.add_new_credit_card(card_number,card_code)

    """
    La prueba test_add_comment comprueba la funcionalidad de agregar comentarios al conductor cuando se escoge la tarifa Comfort
    """
    def test_add_comment(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        comment = data.MESSAGE_FOR_DRIVER
        routes_page.add_comment(comment)
        assert routes_page.get_comment() == comment

    """
    La prueba test_add_blanket_and_scarves comprueba la funcionalidad de agregar mantas y pañuelos cuando se escoge la tarifa Comfort
    """

    def test_add_blanket_and_scarves(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.add_blanket_and_scarves()

    """
    La prueba test_add_chocolate_ice_cream comprueba la funcionalidad de agregar dos helados de chocolate cuando se escoge la tarifa Comfort
    """

    def test_add_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream()

    """
    La prueba test_view_modal_find_taxi comprueba la funcionalidad de el boton para pedir eñ taxi una vez los campos necesarios se llenen de manera correcta
    """
    def test_view_modal_find_taxi(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.book_taxi()


    """
    La prueba test_view_driver_information lleva a cabo la validancion de todo el proceso y al final hace una espera para ver la informacion del conductor
    """

    def test_view_driver_information(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.wait_driver_information()




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
