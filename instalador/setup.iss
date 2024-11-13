; Script de instalación para el proyecto Sistema de Ayuda

[Setup]
AppName=Sistema de Ayuda
AppVersion=1.0
DefaultDirName={pf}\Sistema_de_Ayuda
DefaultGroupName=Sistema de Ayuda
OutputBaseFilename=Sistema_de_Ayuda_Installer
Compression=lzma
SolidCompression=yes

[Files]
; Ejecutable principal
Source: "C:\xampp\htdocs\Sistema_de_Ayuda\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

; Archivos de configuración
Source: "C:\xampp\htdocs\Sistema_de_Ayuda\config.ini"; DestDir: "{app}"; Flags: ignoreversion

; Archivo README y Script de la instalacion
Source: "C:\xampp\htdocs\Sistema_de_Ayuda\README.md"; DestDir: "{app}"; Flags: ignoreversion

Source: "C:\xampp\htdocs\Sistema_de_Ayuda\instalador\setup.iss"; DestDir: "{app}"; Flags: ignoreversion

; Carpeta con los archivos HTML
Source: "C:\xampp\htdocs\Sistema_de_Ayuda\html_files\*"; DestDir: "{app}\html_files"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Sistema de Ayuda"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,Sistema de Ayuda}"; Flags: nowait postinstall skipifsilent
