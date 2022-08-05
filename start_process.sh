#!/bin/bash

pip install pipenv

pipenv install --system

mv template.html /src/teste-pdf/templates/proposta_judicial.html

python /src/teste-pdf/main.py 
