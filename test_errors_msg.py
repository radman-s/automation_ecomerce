from pages.drivers import Drivers
from pages.ecomerce_page import EcomecrePage

browser = Drivers('--start-maximized').chrome()
rp = EcomecrePage(driver=browser)

# Test:  Verify invalid email address error.
rp.go()
rp.sign_in.click()
rp.email_input.input_text('myemail@gmail.com')
rp.create_acc.click()
email_err = rp.invalid_email.text
assert email_err == 'Invalid email address.'
print(f'error msg: {email_err}, validated.')
browser.quit()

# Test: Verify error messages for mandatory fields.
rp.go()
rp.sign_in.click()
rp.email_input.input_text('email_01_@gmail.com')
rp.create_acc.click()
rp.register.click()
msg_error = rp.mandatory.text

expected_error = "There are 8 errors\n\
You must register at least one phone number.\n\
lastname is required.\n\
firstname is required.\n\
passwd is required.\n\
address1 is required.\n\
city is required.\n\
The Zip/Postal code you've entered is invalid. It must follow this format: 00000\n\
This country requires you to choose a State."

assert msg_error == expected_error
print(f'Error message:\n{msg_error},\nvalidated.')
browser.quit()
print('test passed')
















