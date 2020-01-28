import selenium
from selenium.webdriver.common.keys import Keys

browser = selenium.webdriver.Safari()

browser.get('http://www.amazon.com')
assert 'Amazon' in browser.title

browser.implicitly_wait(5)
browser.maximize_window()

elem = browser.find_element_by_id('twotabsearchtextbox')  # Find the search box
elem.send_keys('testing' + Keys.RETURN)

searchresults = browser.find_elements_by_xpath('//div[@class="a-section a-spacing-none"]/h2/a/span')

for el in searchresults:
    print el.text


browser.quit()

