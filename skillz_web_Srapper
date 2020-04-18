from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.implicitly_wait(3)

driver.get("https://games.skillz.com")
driver.find_element_by_xpath('//*[@id="most_popular"]/div/span[2]').click()
driver.implicitly_wait(10)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
title_list=soup.find_all('span', class_='listViewCellText__title text_color_primary')
description_list=soup.find_all('span',class_='listViewCellText__description text_color_primary')
genre_list=soup.find_all('span',class_='listViewCellText__genre theme_color')

title_name=[]
description_name=[]
genre_name=[]
for title in title_list:
    title_name.append(title.text)
for description in description_list:
    description_name.append(description.text)
for genre in genre_list:
    genre_name.append(genre.text)
data=[title_name,description_name,genre_name]
new_data=np.transpose(data)
df=pd.DataFrame(new_data)
df.to_csv('path\\file_name.csv')
