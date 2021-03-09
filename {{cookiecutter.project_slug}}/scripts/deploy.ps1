New-Variable -Name "PROJECT_UNDERSCORE" -Value "{{cookiecutter.project_underscore}}"
New-Variable -Name "PROJECT_SLUG" -Value "{{cookiecutter.project_slug}}"
Write-Output "========= Cleaing up deploy directory ========="
Remove-Item G:\IT\Python\Applications\$PROJECT_SLUG\ -Recurse -Force -Confirm:$false
Write-Output "================ Copying Files ================"
Copy-Item -Path .\dist\$PROJECT_SLUG -Destination G:\IT\Python\Applications\$PROJECT_SLUG\ -Recurse -Force
