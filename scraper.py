from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:/\Users\\pc\\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scrape = []

# Define Exoplanet Data Scrapping Method
def scrape_more_data(hyperlink):

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        page= requests.get(hyperlink)
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")
        
        temp_list=[]
        
        for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tags=tr_tag.find_all("td")
        for td_tag in td_tags:
            try:
               temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0]) 
            except:
                temp_list.append("")
        scrape.append(temp_list)

        
        

        # Find all elements on the page and click to move to the next page
    browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "Radius", "Luminosity"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(scrape, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
    