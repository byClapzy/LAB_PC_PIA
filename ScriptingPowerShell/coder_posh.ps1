#Limpiando pantalla
#Edgar Fernando Gonzalez Pardavé
#2030467
Clear-Host
#Mensaje de bienvenida
Write-Host "Ejemplo de codificador de Base64 en Powershell" -ForegroundColor Yellow
Write-Host "Escribe una frase a codificar: "-ForegroundColor Yellow
#Solicitamos la entrada de una cadena de texto.
$frase= Read-Host
#Codificador en Base64 y guardando resultado en una cadena.
$encod= [convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes(($frase)))
#Imprimiendo la salida
Write-Host "La frase escrita en Base 64 es: "-ForegroundColor Green
Write-Output $encod