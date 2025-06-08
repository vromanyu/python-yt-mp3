#!/bin/bash

function build-program() {
  source .venv/bin/activate
  pyinstaller -F --paths=.\.venv\Libs\site-packages converter.py
  deactivate
}

build-program
