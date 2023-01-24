from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
date = now.strftime("%d%m%Y")



website = "https://www.coindesk.com/livewire/"
path = '/usr/local/bin/chromedriver'

#headless mode
options = Options()
options.headless = True
s=Service(executable_path=path)
driver = webdriver.Chrome(service=s, options=options)

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="article-cardstyles__AcTitle-q1x8lc-1 bzAuaw articleTextSection "]')

titles = []
links = []

for container in containers:
	title = container.find_element(by="xpath", value='./h5').text
	link = container.find_element(by="xpath", value='./h5/a').get_attribute("href")

	titles.append(title)
	links.append(link)

driver.quit()

mydictionary = {'Title': titles, 'Link': links}

df_news = pd.DataFrame(mydictionary)
file_name = f'cryptonews_{date}.csv'

final_path = os.path.join(application_path, file_name)

df_news.to_csv(final_path)

