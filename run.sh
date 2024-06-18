#!/bin/sh
set -eu
. ./venv/bin/activate
flake8 ./main.py
mypy ./main.py
./main.py
