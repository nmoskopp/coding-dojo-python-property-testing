#!/bin/sh
set -eu
python3 -m venv .
. ./bin/activate
pip3 install -r requirements.txt