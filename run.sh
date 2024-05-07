#!/bin/sh
set -eu
. ./bin/activate
flake8 ./main.py
mypy ./main.py
./main.py
