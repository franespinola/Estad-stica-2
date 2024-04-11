from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Inicializar el driver de Selenium
driver = webdriver.Chrome()
driver.get("https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/all-time")
time.sleep(2)

# Función para obtener datos de una página
def obtener_datos_pagina():
    ranks = driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center[1]/table/tbody/tr/td[1]')
    released_worldwide = driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center/table/tbody/tr/td[2]/a')
    titles = driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center/table/tbody/tr/td[3]/b/a')
    worldwide_box_office = driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center/table/tbody/tr/td[4]')
    domestic_box_office = driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center/table/tbody/tr/td[5]')
    international_box_office = driver.find_elements(By.XPATH,'//*[@id="page_filling_chart"]/center/table/tbody/tr/td[6]')

    rankings_generales = []

    for i in range(len(titles)):
        ranking_general = {'Rank':ranks[i].text,
                           'Released Worldwide':released_worldwide[i].text,
                           'Title':titles[i].text,
                           'Domestic box officce':domestic_box_office[i].text,
                           'International Box Office':international_box_office[i].text,
                           'Worldwide Box Office':worldwide_box_office[i].text
                           }
        rankings_generales.append(ranking_general)
    return rankings_generales

# Obtener datos de todas las páginas
all_rankings = []
current_page = 1

while True:
    print("Obteniendo datos de la página:", current_page)
    all_rankings.extend(obtener_datos_pagina())
    next_page_button = driver.find_element(By.XPATH, '//*[@id="page_filling_chart"]/center/div/a[2]')
    if next_page_button.get_attribute('href'):
        next_page_button.click()
        current_page += 1
        time.sleep(2)
    else:
        break

# Crear DataFrame y guardar en archivos CSV y Excel
df = pd.DataFrame(all_rankings)
print(df)
df.to_csv('rankings_generales.csv',index=False)
df.to_excel('rankings_generales.xlsx',index=False)

# Cerrar el navegador
driver.quit()
