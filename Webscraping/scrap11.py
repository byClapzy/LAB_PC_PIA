#Importación de modulos
import requests
from bs4 import BeautifulSoup
# Obtención de los datos mediante petición GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Analizamos el contendio HTML con BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")
# Buscar todos los elementos que el h2 contenga en su texto
# la palabra "python"
python_jobs = results.find_all(
    "h2", string = lambda text: "python" in text.lower()

    )
# Buscar cada elemento que tenga referencia de python_jobs
#y almacenarlo en python _jobs_elements
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
    ]
# Mostrar informacion de python_jobs_elemnts
for job_element in python_jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # Buscamos elementos con la etiqueta "a"
    links = job_element.find_all("a")
    print(company_element.text.strip())
    print(location_element.text.strip()) 
    print(title_element.text.strip())
    # Mostramos todos los elementos de lnks
    for link in links:
        link_url = link["href"]
        #Formateamos el orint para que incluye el link
        print(f"Apply Here: {link_url}\n")
    print()