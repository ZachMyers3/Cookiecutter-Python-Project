New-Variable -Name "PROJECT_UNDERSCORE" -Value "{{cookiecutter.project_underscore}}"
New-Variable -Name "PROJECT_SLUG" -Value "{{cookiecutter.project_slug}}"
Write-Output "Cleaing up build directories"
Remove-Item .\build\* -Recurse -Force -Confirm:$false
Remove-Item .\dist\* -Recurse -Force -Confirm:$false
Write-Output "Building executables"
poetry run pyinstaller $PROJECT_UNDERSCORE/cli.py --name $PROJECT_SLUG --noconfirm
Write-Output "Build complete!"
