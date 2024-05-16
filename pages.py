from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import helpers



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    get_taxi_button = (By.XPATH, "//button[@type='button' and contains(@class, 'button') and contains(text(), 'taxi')]")
    comfort_tariff_button = (By.XPATH, "//img[contains(@src, '/static/media/kids') and @alt='Comfort']")
    add_new_phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_field = (By.ID, "phone")
    phone_code_field = (By.XPATH, "//*[@id='code']")
    next_window_phone_number = (By.CSS_SELECTOR, '.number-picker > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > button:nth-child(1)')
    confirm_code_phone_button = (By.CSS_SELECTOR, ".number-picker > div:nth-child(2) > div:nth-child(2) > form:nth-child(3) > div:nth-child(2) > button:nth-child(1)")
    close_phone_number_window = (By.CSS_SELECTOR, ".number-picker > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)")
    payment_method_button = (By.CLASS_NAME, "pp-text")
    create_new_credit_card_button = (By.CLASS_NAME, "pp-plus")
    credit_card_number_field = (By.ID,  "number")
    credit_card_code_field = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    add_credit_card = (By.CSS_SELECTOR, "html body div#root div.app div.payment-picker.open div.modal.unusual div.section.active.unusual form div.pp-buttons button.button.full")
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
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        return self.driver.find_element(*self.comfort_tariff_button).click()


    def add_new_phone_number(self,phone_number):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.add_new_phone_number_button))
        self.driver.find_element(*self.add_new_phone_number_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)
        self.driver.find_element(*self.next_window_phone_number).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.phone_code_field))
        self.driver.find_element(*self.phone_code_field).send_keys(helpers.retrieve_phone_code(self.driver))
        self.driver.find_element(*self.confirm_code_phone_button).click()


    def get_phone_number_field_value(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')


    def add_new_credit_card(self,credit_card_number,credit_card_code):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.payment_method_button))
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
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.add_credit_card))
        self.driver.find_element(*self.add_credit_card).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.close_payment_method_window))
        self.driver.find_element(*self.close_payment_method_window).click()

    def add_comment(self,comment):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comments_field))
        self.driver.find_element(*self.comments_field).send_keys(comment)

    def get_comment(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comments_field))
        return self.driver.find_element(*self.comments_field).get_property('value')

    def add_blanket_and_scarves(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.add_blanket_and_scarves_switch))
        element = self.driver.find_element(*self.add_blanket_and_scarves_switch)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def add_ice_cream(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.add_ice_cream_button))
        element = self.driver.find_element(*self.add_ice_cream_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        element.click()



    def book_taxi(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comments_field))
        self.driver.find_element(*self.comments_field).send_keys(data.MESSAGE_FOR_DRIVER)
        self.driver.find_element(*self.payment_method_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.create_new_credit_card_button))
        self.driver.find_element(*self.create_new_credit_card_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.credit_card_number_field))
        self.driver.find_element(*self.credit_card_number_field).clear()
        self.driver.find_element(*self.credit_card_number_field).send_keys(data.CARD_NUMBER)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.credit_card_code_field))
        self.driver.find_element(*self.credit_card_code_field).clear()
        self.driver.find_element(*self.credit_card_code_field).send_keys(data.CARD_CODE)
        self.driver.find_element(*self.credit_card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*self.add_credit_card).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.close_payment_method_window))
        self.driver.find_element(*self.close_payment_method_window).click()
        self.driver.find_element(*self.book_taxi_button).click()

    def wait_driver_information(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.get_taxi_button))
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comfort_tariff_button))
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.comments_field))
        self.driver.find_element(*self.comments_field).send_keys(data.MESSAGE_FOR_DRIVER)
        self.driver.find_element(*self.payment_method_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.create_new_credit_card_button))
        self.driver.find_element(*self.create_new_credit_card_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.credit_card_number_field))
        self.driver.find_element(*self.credit_card_number_field).clear()
        self.driver.find_element(*self.credit_card_number_field).send_keys(data.CARD_NUMBER)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.credit_card_code_field))
        self.driver.find_element(*self.credit_card_code_field).clear()
        self.driver.find_element(*self.credit_card_code_field).send_keys(data.CARD_CODE)
        self.driver.find_element(*self.credit_card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*self.add_credit_card).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.close_payment_method_window))
        self.driver.find_element(*self.close_payment_method_window).click()
        self.driver.find_element(*self.book_taxi_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.waiting_counter))
        element = self.driver.find_element(*self.waiting_counter)
        WebDriverWait(self.driver, 60).until(lambda driver: element.text == "00:01")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.book_details_button))
        self.driver.find_element(*self.book_details_button).click()
