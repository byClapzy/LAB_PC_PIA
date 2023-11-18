Clear-Host
Write-Host "Bienvenido a un ejemplo de codificación / decodificación base64 usando powershell" -ForegrounColor Green
Write-Host "Codificando un archivo de texto"
#
# Se va a leer el contenido del archivo de texto
#
$inputfile="C:\Users\edgar\Desktop\LAB\Tareas_LAB\Scripts07_2030467\secret.txt"
$fc= get-content $inputfile
$GB= [System.Text.Encoding]::UTF8.Getbytes($fc)
$etext=[System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green
#
# Decodificando contento de un archivo
#
Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" c:\Users\edgar\Desktop\LAB\Tareas_LAB\Scripts07_2030467\decode_secret.txt
$outfile12= get-content c:\Users\edgar\Desktop\LAB\Tareas_LAB\Scripts07_2030467\decode_secret.txt
Write-Host "El texto decodificado es el siguiente:" -ForegrounColor Green
Write-Host "DECODIFICADO:" $outfile12