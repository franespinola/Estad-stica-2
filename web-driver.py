from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Inicializar el driver de Selenium
driver = webdriver.Chrome()
driver.get("https://www.the-numbers.com/movies/report/All/All/All/All/All/All/All/All/All/None/None/None/None/None/None/None/None/None/None?view-order-by=worldwide-box-office&view-order-direction=desc&show-production-budget=On&show-opening-weekend-theaters=On&show-domestic-box-office=On&show-maximum-theaters=On&show-inflation-adjusted-domestic-box-office=On&show-theatrical-engagements=On&show-international-box-office=On&show-opening-weekend-revenue=On&show-worldwide-box-office=On&show-worldwide-release-year=On&show-theatrical-distributor=On&show-genre=On&show-source=On&show-production-method=On&show-creative-type=On")
time.sleep(2)
titles=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[3]/b/a')
ranks=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[1]')
released_worldwide=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[2]')
theatrical_distributor=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[4]/a')
genre=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[5]/a')
source=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[6]/a')
production_method=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[7]/a')
creative_type=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[8]/a')
production_budget=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[9]')
opening_weekend_theaters=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[10]')
maximum_theaters=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[11]')
theatrical_engagements=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[12]')
opening_weekend_revenue=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[13]')
domestic_box_office=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[14]')
inf_adj_domestic_box_office=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[15]')
international_box_office=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[16]')
worldwide_box_office=driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[17]')


rankings_generales = []

for i in range(len(titles)):
    ranking_general = {'Rank':ranks[i].text,
                       'Released Worldwide':released_worldwide[i].text,
                       'Title':titles[i].text,
                       'Theatrical Distributor':theatrical_distributor[i].text,
                       'Genre':genre[i].text,
                       'Source':source[i].text,
                       'Production Method':production_method[i].text,
                       'Creative Type':creative_type[i].text,
                       'Production Budget':production_budget[i].text,
                       'Opening Weekend Theaters':opening_weekend_theaters[i].text,
                       'Maximum Theaters':maximum_theaters[i].text,
                       'Theatrical Engagements':theatrical_engagements[i].text,
                       'Opening Weekend Revenue':opening_weekend_revenue[i].text,
                       'Domestic box officce':domestic_box_office[i].text,
                       'Inf Adj Domestic Box Office':inf_adj_domestic_box_office[i].text,
                       'International Box Office':international_box_office[i].text,
                       'Worldwide Box Office':worldwide_box_office[i].text
                       }
    rankings_generales.append(ranking_general)
print(rankings_generales)

df = pd.DataFrame(rankings_generales)
print(df)
df.to_csv('rankings_generales.csv',index=False)
df.to_excel('rankings_generales.xlsx',index=False)
