#Importat modulos
#Edgar Fernando Gonzlaez Pardavé 
#2030467
import requests
import csv
from bs4 import BeautifulSoup
#Direccion de la pagina web
url = "http://quotes.toscrape.com/"
#Ejecutat GET-Request
response = requests.get(url)
#Anilazar sinteticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
#Extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
#Crea una lista de las citas
quotes= list()
for quote in quotes_html:
	quotes.append(quote.text)
#Crea una lista de los autores
authors = list()
for author in authors_html:
	authors.append(author.text)
#Para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
	print (t)
#Guarlas las citas y autores en un archivo CSV en el directorio acutal
#Abrir el archivo con Excel  / LibreOffice, etc.
with open ('./citas_2030467.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file, dialect='excel')
	csv_writer.writerows(zip(quotes, authors))