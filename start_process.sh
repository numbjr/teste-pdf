#!/bin/bash

pip install pipenv

pipenv install --system

mv tmp/template.html templates/proposta_judicial.html

python main.py 
