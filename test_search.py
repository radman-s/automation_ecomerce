from pages.ecomerce_page import EcomecrePage
from pages.drivers import Drivers

browser = Drivers('--start-maximized').chrome()
ep = EcomecrePage(driver=browser)

# Test
# name of a product to be submitted to the search. Verify the name of the search output
# to be same as the submitted item name.
# test setup
mail = 'email222@gmail.com'
passw = 'password'

ep.go()
ep.sign_in.click()
ep.email_input.input_text(mail)
ep.pw.input_text(passw)
ep.log_in.click()
ep.women_but.move_to()
ep.sub_tshirt.click()
ep.product1.move_to()
name1 = ep.product1_name.text
ep.search_input.input_text(name1)
ep.search_submit.click()
name2 = ep.product1_name.text
assert name1 == name2
print(f'original item name: {name1}\nsearch item name: {name2}.')
browser.quit()
print('test passed')

