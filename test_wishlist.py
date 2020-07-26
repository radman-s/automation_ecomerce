from pages.ecomerce_page import EcomecrePage
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

ec = EcomecrePage(driver=browser)

# Test: Verify that 'Add to Wishlist' only works after login.
ec.go()
ec.women_but.move_to()
ec.sub_tshirt.click()
ec.product1.move_to()
ec.add_wishlist.click()
error_msg = ec.log_in_err.text
assert error_msg == 'You must be logged in to manage your wishlist.'
print(f'{error_msg}, validated.')
browser.quit()







