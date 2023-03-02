#!/bin/sh
pip3 install -r datasource-py/requirements.txt
pip3 install -r nlp/requirements.txt
python -m spacy download en_core_web_sm
