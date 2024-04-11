from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Inicializar el driver de Selenium
driver = webdriver.Chrome()

# Función para obtener datos de una página
def obtener_datos_pagina(url):
    driver.get(url)
    time.sleep(2)
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
                           'Worldwide Box Office':worldwide_box_office[i].text,
                           'Domestic box officce':domestic_box_office[i].text,
                           'International Box Office':international_box_office[i].text
                           }
        rankings_generales.append(ranking_general)
    return rankings_generales

# Obtener datos de todas las páginas
all_rankings = []
base_url = "https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/all-time/"
current_page = 1

while True:
    print("Obteniendo datos de la página:", current_page)
    url = f"{base_url}{current_page}"
    all_rankings.extend(obtener_datos_pagina(url))
    current_page += 100  # Incrementa en 100 para pasar a la siguiente página
    if len(all_rankings) % 100 != 0:
        # Si el número de elementos en la lista no es un múltiplo de 100, hemos alcanzado la última página
        break

# Crear DataFrame y guardar en archivos CSV y Excel
df = pd.DataFrame(all_rankings)
print(df)
df.to_csv('rankings_generales.csv',index=False)
df.to_excel('rankings_generales.xlsx',index=False)

# Cerrar el navegador
driver.quit()

