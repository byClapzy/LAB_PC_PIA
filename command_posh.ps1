#
# Comando de powershell a codificar en Base64
#
$comando = 'Get-Wmiobject win32_logicaldisk | foreach {Write-Host $_.deviceID $_.size $_.freespace}'
#
# codificando $comando
#
$encod= [convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($comando))
Write-Host $encode
#
# Ejecutando el comando codificado
#
Write-Host "Vams a ejecutar el comando asi: powershell -E "$encode -ForegroundColor cyan
Start-Sleep 1
powershell -E $encode
#
Start-Sleep 2
#
# $comando_secret guarda un comando codificado en Base64
#
$comando_secret='RwBlAHQALQBXAG0AaQBPAGIAagBlAGMAdAAgAHcAaQBuADMAMgBfAGIAYQBzAGUAcwBlAHIAdgBpAGMAZQAgAHwAZgBvAHIAZQBhAGMAaAAgAHsAVwByAGkAdABlAC0ASABvAHMAdAAgACQAXwAuAGQAaQBzAHAAbABhAHkAbgBhAG0AZQAgACQAXwAuAHMAdABhAHQAZQB9AA=='
#
# Decodificaremos el comando 
$decod=[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($comando_secret))
#
## Mostramos el  resultado
#
Write-Host "El comando codificado es :" -ForegrounColor Cyan
Write-Host $comando_secret
Write-Host ""
Write-Host "El comando ya sin codificar :" -ForegroundColor Cyan
Write-Host $decod
