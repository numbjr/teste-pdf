#!/bin/bash

pip install pipenv

pipenv install --system

mv template.html templates/proposta_judicial.html

python main.py 
