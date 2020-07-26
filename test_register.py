from selenium import webdriver
from pages.ecomerce_page import EcomecrePage

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

ec = EcomecrePage(driver=browser)

# test setup
email = 'test_01_@gmail.com'
pw_test = 'testpw0000'
f_name = 'Joe'
l_name = 'Jones'
comp_name = 'SuperComp'
adr1 = 'Wilson rd, P.O.Box, SuperComp'
adr2 = 'Aparnemt, 4, 20, floor-5'
cit = 'Trinec'
zp = '73961'
hp = '00420784521478'
mp = '00420254441145'
ali = 'alias@gmail.com'

# Test: registration procedure.
ec.go()
ec.sign_in.click()
ec.email_input.input_text(email)
ec.create_acc.click()
ec.title_mrs.click()
ec.title_mr.click()
ec.first_name.input_text(f_name)
ec.last_name.input_text(l_name)
ec.pw.input_text(pw_test)
ec.day_birth.select_drop('3')
ec.month_birth.select_drop('6')
ec.year_birth.select_drop('1980')
ec.company.input_text(comp_name)
ec.addres1.input_text(adr1)
ec.addres2.input_text(adr2)
ec.city.input_text(cit)
ec.state.select_drop('43')
ec.add_info.input_text('here is more info')
ec.home_phone.input_text(hp)
ec.mobile_phone.input_text(mp)
ec.alias.input_text(ali)
ec.register.click()
browser.quit()
print('Test successful.')

















