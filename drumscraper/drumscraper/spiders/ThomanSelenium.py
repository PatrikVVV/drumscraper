import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize the ChromeService
service = Service(r'C:\Users\patri\OneDrive - HvA\ODM\Chrome')

# Create a Chrome driver instance with the service
driver = webdriver.Chrome()

driver.get('https://www.thomann.de/nl/index.html')

time.sleep(5) # Let the user actually see something!

decline = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button[2]')
decline.click()

# Locate the search box and send keys
search_box = driver.find_element(By.XPATH, '//*[@id="fsearch-sw"]')
search_box.send_keys('complete drumstellen')

# Submit the search
search_box.submit()

time.sleep(5) # Let the user actually see something!

# Quit the driver
driver.quit()


#!/usr/bin/env python
print('If you get error "ImportError: No module named \'six\'" install six:\n'+\
    '$ sudo pip install six');
print('To enable your free eval account and get CUSTOMER, YOURZONE and ' + \
    'YOURPASS, please contact sales@brightdata.com')
import sys
if sys.version_info[0]==2:
    import six
    from six.moves.urllib import request
    opener = request.build_opener(
        request.ProxyHandler(
            {'http': 'http://brd-customer-hl_79cc5ce7-zone-residentialproxy12-country-nl:513hewuu6yp7@brd.superproxy.io:22225',
            'https': 'http://brd-customer-hl_79cc5ce7-zone-residentialproxy12-country-nl:513hewuu6yp7@brd.superproxy.io:22225'}))
    print(opener.open('https://www.thomann.de/nl/index.html').read())
if sys.version_info[0]==3:
    import urllib.request
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {'http': 'http://brd-customer-hl_79cc5ce7-zone-residentialproxy12-country-nl:513hewuu6yp7@brd.superproxy.io:22225',
            'https': 'http://brd-customer-hl_79cc5ce7-zone-residentialproxy12-country-nl:513hewuu6yp7@brd.superproxy.io:22225'}))
    print(opener.open('https://www.thomann.de/nl/index.html').read())