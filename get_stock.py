from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
os.environ['WDM_LOG_LEVEL'] = '0'

def crawl():
  pc_header = [
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36', #chrome 88
  ]
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('blink-settings=imagesEnabled=false') #이미지 로딩 X
  chrome_options.add_argument('headless') #창 띄우지않음
  chrome_options.add_argument("disable-gpu")
  chrome_options.add_argument("lang=ko_KR")
  chrome_options.add_argument('--incognito')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument(f"user-agent={pc_header}")
  chrome_options.add_argument('--disable-blink-features=AutomationControlled')
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  chrome_options.add_argument('--ignore-certificate-errors')
  chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
  chrome_options.add_experimental_option('useAutomationExtension', False)
  chrome_options.add_argument("--disable-setuid-sandbodx")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--disable-infobars")
  chrome_options.add_argument("--disable-browser-side-navigation")
  prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}  
  chrome_options.add_experimental_option('prefs', prefs)
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
  driver.implicitly_wait(30) 
  driver.get("https://finance.daum.net/")
  time.sleep(1)
  
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  stocks = soup.find("div",{"class":"rankingB"}).find_all("li")
  top_stocks = []
  for i in stocks:
    top = i.find("a")
    top_stocks.append({"stock_name":top.text,"stock_code":top['href'][top['href'].rfind("A")+1:]})
  
  driver.quit()

  return top_stocks