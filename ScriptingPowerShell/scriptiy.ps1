$tarea = New-ScheduledTaskAction -Execute C:\Users\edgar\Desktop\cosas_guardadas\LAB\Tareas_LAB\Practica15_2030467\send_syinfo.ps1

$triggers = New-ScheduledTaskTrigger -Once -At 8:25pm


Register-ScheduledTask -Action $tarea -Trigger $triggers -TaskPath "MisTareas" -TaskName "Enviar sysinfo" -Description "Envio de informacion del sistema"
