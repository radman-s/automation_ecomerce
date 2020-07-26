from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locator import Locator
from .base_element import BaseElement

class EcomecrePage(BasePage):

    url = 'http://automationpractice.com/index.php'


    @property
    def sign_in(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="Log in to your customer account"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def log_in(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="SubmitLogin"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def email_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="email_create"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def create_acc(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="SubmitCreate"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def title_mr(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="id_gender1"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def title_mrs(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="id_gender2"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def first_name(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="customer_firstname"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def last_name(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="customer_lastname"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def pw(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="passwd"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def day_birth(self):
        locator = Locator(By.XPATH, '//select[@id="days"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def month_birth(self):
        locator = Locator(By.XPATH, '//select[@id="months"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def year_birth(self):
        locator = Locator(By.XPATH, '//select[@id="years"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def company(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="company"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def addres1(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="address1"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def addres2(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="address2"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def city(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="city"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def state(self):
        locator = Locator(By.XPATH, '//select[@id="id_state"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def zip_code(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="postcode"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def country(self):
        locator = Locator(By.XPATH, '//select[@id="id_country"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def add_info(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[id="other"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def home_phone(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="phone"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def mobile_phone(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="phone_mobile"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def alias(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="alias"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def register(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="submitAccount"]')
        return BaseElement(dirver=self.driver, locator=locator)

    # ERROR MESSAGES
    @property
    def invalid_email(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="create_account_error"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def mandatory(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="alert alert-danger"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def reg_email(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="email"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def reg_pw(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="passwd"]')
        return BaseElement(dirver=self.driver, locator=locator)

    # Order a product
    @property
    def women_but(self):
        locator = Locator(By.XPATH, '//a[text()="Women"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def sub_tshirt(self):
        locator = Locator(By.XPATH, '(//a[text()="T-shirts"])[1]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def product1(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="product-image-container"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def product1_name(self):
        locator = Locator(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[1]/div[1]/div[2]/h5[1]/a[1]")
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def more(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="View"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def q_up(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="btn btn-default button-plus product_quantity_up"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def size(self):
        locator = Locator(By.XPATH, '//select[@id="group_1"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def color_bl(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="color_14"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def add_card(self):
        locator = Locator(By.CSS_SELECTOR, 'button[name="Submit"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def proceed_1(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="Proceed to checkout"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def proceed_2(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="http://automationpractice.com/index.php?controller=order&step=1"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def proceed_3(self):
        locator = Locator(By.XPATH, '(//button[@type="submit"])[2]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def pay_wire(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="Pay by bank wire"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def confirm_order(self):
        locator = Locator(By.CSS_SELECTOR, 'button[class="button btn btn-default button-medium"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def confirm_msg(self):
        locator = Locator(By.XPATH, '//h1[text()="Order confirmation"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def add_wishlist(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="addToWishlist wishlistProd_1"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def log_in_err(self):
        locator = Locator(By.XPATH, '//p[text()="You must be logged in to manage your wishlist."]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def q_up_summary(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="Add"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def total_value(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="total_price"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def search_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="search_query_top"]')
        return BaseElement(dirver=self.driver, locator=locator)

    @property
    def search_submit(self):
        locator = Locator(By.CSS_SELECTOR, 'button[name="submit_search"]')
        return BaseElement(dirver=self.driver, locator=locator)




