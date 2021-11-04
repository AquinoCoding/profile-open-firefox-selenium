from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("-profile")
options.add_argument("/home/aquino/.mozilla/firefox/nxq0n4mh.default-release")

driver = webdriver.Firefox(options=options,
            executable_path=r'/home/aquino/Documentos/newcontactZap/geckodriver')

requestJsonCelular = '5561993786281'
urlWhatsApp = 'http://api.whatsapp.com/send?phone=+'


urlDefinition = urlWhatsApp + requestJsonCelular

driver.get(urlDefinition)