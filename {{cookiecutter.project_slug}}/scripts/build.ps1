New-Variable -Name "NAME" -Value "{{cookiecutter.project_slug}}"
Write-Output "Cleaing up build directories"
Remove-Item .\build\* -Recurse -Force -Confirm:$false
Remove-Item .\dist\* -Recurse -Force -Confirm:$false
Write-Output "Building executables"
poetry run pyinstaller $NAME/cli.py --name $NAME --noconfirm
Write-Output "Build complete!"
