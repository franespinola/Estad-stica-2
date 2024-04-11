from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Inicializar el driver de Selenium
driver = webdriver.Chrome()
driver.get("https://www.the-numbers.com/movies/report/All/All/All/All/All/All/All/All/All/None/None/None/None/None/None/None/None/None/None?view-order-by=worldwide-box-office&view-order-direction=desc")
time.sleep(2)
titles=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[2]/b/a')
ranks=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[1]')

rankings_generales = []

for i in range(len(titles)):
    ranking_general = {'rank':ranks[i].text,'title':titles[i].text}
    rankings_generales.append(ranking_general)
print(rankings_generales)

df = pd.DataFrame(rankings_generales)
print(df)
df.to_csv('rankings_generales.csv',index=False)
df.to_excel('rankings_generales.xlsx',index=False)





