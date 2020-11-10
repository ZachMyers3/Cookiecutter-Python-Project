New-Variable -Name "NAME" -Value "{{cookiecutter.project_slug}}"
Write-Output "Cleaing up build directories"
Remove-Item .\build\* -Recurse -Force -Confirm:$false
Remove-Item .\dist\* -Recurse -Force -Confirm:$false
Write-Output "Building executables"
poetry run pyinstaller cow_ftp/cli.py --name $NAME --noconfirm --hidden-import=cow_libr --hidden-import=cow_compile --hidden-import=cow_get
Write-Output "Copying files"
Copy-Item .\cow_ftp\static .\dist\$NAME\static
Write-Output "Build complete!"
