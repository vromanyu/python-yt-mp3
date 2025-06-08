#!/bin/bash

function build-program() {
  source .venv/Scripts/activate
  pyinstaller -F --paths=.\.venv\Libs\site-packages converter.py
  deactivate
}

build-program
