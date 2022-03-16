from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://bodyvisualizer.com/')
sleep(10)
print(driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/span').text)
