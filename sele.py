from pkgutil import ModuleInfo
from turtle import screensize
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from parm_option import ParmOptions 
from time import sleep

def change_parm(type_xpath,monitor_path,check):
    print("check:",check)
    ele =driver.find_element_by_xpath(type_xpath)
    monitor=driver.find_element_by_xpath(monitor_path)
    if(int(monitor.text)>check):
        while True:
            ele.click()
            ele.send_keys(Keys.ARROW_LEFT)
            if(int(monitor.text)==check):
                break
    elif(int(monitor.text)<check):
        while True:
            ele.click()
            ele.send_keys(Keys.ARROW_RIGHT)
            if(int(monitor.text)==check):
                break
    else:
        return
    print('out')


opt = ParmOptions().parse()
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56")
options.add_argument("disable-gpu")
options.add_argument('window-size=1920x1080')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.
url ='https://bodyvisualizer.com/'


### Xpath
height=['/html/body/div[1]/div[5]/div[2]/div[1]/div[4]/a','/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/span']
weight=['/html/body/div[1]/div[5]/div[2]/div[2]/div[4]/a','/html/body/div[1]/div[5]/div[2]/div[2]/div[2]/span']
chest=['/html/body/div[1]/div[5]/div[2]/div[3]/div[4]/a','/html/body/div[1]/div[5]/div[2]/div[3]/div[2]/span']
waist=['/html/body/div[1]/div[5]/div[2]/div[4]/div[4]/a','/html/body/div[1]/div[5]/div[2]/div[4]/div[2]/span']
hips=['/html/body/div[1]/div[5]/div[2]/div[5]/div[4]/a','/html/body/div[1]/div[5]/div[2]/div[5]/div[2]/span']
inseam=['/html/body/div[1]/div[5]/div[2]/div[6]/div[4]/a','/html/body/div[1]/div[5]/div[2]/div[6]/div[2]/span']
exercise=['/html/body/div[1]/div[5]/div[2]/div[7]/div[4]/a','/html/body/div[1]/div[5]/div[2]/div[7]/div[2]/span']
### monitor path


body_shape ='/html/body/div[1]/div[4]/div[1]/canvas'

driver.get(url)
sleep(2)

print("################# LOADING ################")


driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[4]/a').click()
sleep(0.5)
### setting parm
print("################# SETTING ################")
change_parm(height[0],height[1],opt.height)
change_parm(weight[0],weight[1],opt.weight)
change_parm(chest[0],chest[1],opt.chest)
change_parm(waist[0],waist[1],opt.waist)
change_parm(hips[0],hips[1],opt.hips)
change_parm(inseam[0],inseam[1],opt.inseam)
change_parm(exercise[0],exercise[1],opt.exercise)

print("screenshot")
### image save
body_shape=driver.find_element_by_xpath(body_shape)
body_shape.screenshot('./body_shape.png')
with open(r"canvas.obj", 'wb') as f:
    f.write(body_shape)

driver.quit()
