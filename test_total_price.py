from pages.ecomerce_page import EcomecrePage
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

ep = EcomecrePage(driver=browser)


# test setup
mail = 'email222@gmail.com'
passw = 'password'

# Test: Verify that Total Price is reflecting correctly if user changes
# quantity on 'Shopping Cart Summary' Page.
ep.go()
ep.sign_in.click()
ep.email_input.input_text(mail)
ep.pw.input_text(passw)
ep.log_in.click()
ep.women_but.move_to()
ep.sub_tshirt.click()
ep.product1.move_to()
ep.more.click()
ep.color_bl.click()
ep.add_card.click()
ep.proceed_1.click()

# compare prices after value change
price1 = ep.total_value.text
print(f'price one item output: {price1}')

ep.q_up_summary.click()
time.sleep(3)

price2 = ep.total_value.text
print(f'price two items output: {price2}')

p1 = float(price1[1:])
p2 = float(price2[1:])
expect_val = p1 * 2
if p2 == expect_val:
    print(f'value output: {p2} is same as expected value: {expect_val}.')
else:
    print(f'value outcome: {p2} not same as expected value: {expect_val}.')
browser.quit()






