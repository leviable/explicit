#!/bin/bash

twine upload --config-file ./.pypirc -r pypi -p $PYPI_PASSWORD dist/*
