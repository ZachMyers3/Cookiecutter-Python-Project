New-Variable -Name "NAME" -Value "{{cookiecutter.project_slug}}"
Write-Output "========= Cleaing up deploy directory ========="
Remove-Item G:\IT\Python\Applications\$NAME\ -Recurse -Force -Confirm:$false
Write-Output "================ Copying Files ================"
Copy-Item -Path .\dist\$NAME -Destination G:\IT\Python\Applications\$NAME\ -Recurse -Force
