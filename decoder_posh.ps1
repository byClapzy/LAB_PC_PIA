#Limpiando pantalla
#Edgar Fernando Gonzalez Pardavé
#2030467
Clear-Host
#Mensaje de bienvenida
Write-Host "Ejemplo de codificador de Base64 en Powershell" -ForegroundColor Yellow
#
# Mensaje codificado en Base 64
#
$texto='TABhAGIAbwByAGEAdABvAHIAaQBvACAAZABlACAAUAByAG8AZwByAGEAbQBhAGMAaQDzAG4AIABwAGEAcgBhACAAQwBpAGIAZQByAFMAZQBnAHUAcgBpAGQAYQBkACAAUwBlAHMAaQDzAG4AIAAxADAA'
Write-Host "La cadena a decodificar es: "
Write-Host $texto
#
# Decodificando mensaje
#
$decod = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($texto))
Write-Host "La cadena ya decodificada es:" -ForegroundColor Green
Write-Host $decod


