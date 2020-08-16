from pages.drivers import Drivers
from pages.ecomerce_page import EcomecrePage

browser = Drivers('--start-maximized').chrome()
ep = EcomecrePage(driver=browser)

# Test setup
mail = 'email222@gmail.com'
passw = 'password'

# Test: product purchase procedure.
ep.go()
ep.sign_in.click()
ep.reg_email.input_text(mail)
ep.reg_pw.input_text(passw)
ep.log_in.click()
ep.women_but.move_to()
ep.sub_tshirt.click()
ep.product1.move_to()
ep.more.click()
ep.q_up.click()
ep.size.move_to()
ep.size.select_drop('3')
ep.color_bl.click()
ep.add_card.click()
ep.proceed_1.click()
ep.proceed_2.click()
ep.proceed_3.click()

# terms and conditions checkbox
browser.find_element_by_css_selector('input[id="cgv"]').click()
ep.proceed_3.click()
ep.pay_wire.click()
ep.confirm_order.click()
comf_msg = ep.confirm_msg.text
assert comf_msg == 'ORDER CONFIRMATION'
print(f'{comf_msg}, validated.')
browser.quit()
print('test passed')























