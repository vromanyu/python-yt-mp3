function Build-Program() {
    .\.venv\Scripts\activate.ps1
    pyinstaller -F --paths=.\.venv\Libs\site-packages converter.py
    deactivate
}

Build-Program