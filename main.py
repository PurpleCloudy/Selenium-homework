import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# def pathfinder(browser:webdriver.Chrome) -> None:
#   product_name 
#   rating
#   number
#   description
#   links
#   price_official
#   price_sale
#   path

def main() -> None:
  options = webdriver.ChromeOptions()
  options.add_argument('--window-size=1920,1080')
  options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
  
  browser = webdriver.Chrome(options=options)
  browser.get('https://kazanexpress.ru/categoryelektronika-10020')
  next_page = 'start_page'
  while True:
    if next_page:
      next_page = browser.find_element(by=By.XPATH("//a[@data-v-794dfa46]")).find_element(by=By.TAG_NAME, value='a')
      print(next_page)
      next_page.click()
    else:
      print(1)
      next_page = None
      break
  
  browser.quit()
    
if __name__ == '__main__':
  main()