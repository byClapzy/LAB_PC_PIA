# Importar módulos
import requests
# Obtener la informalción HTML de la URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# Imprimir el texto de la petición GET
print(page.text)