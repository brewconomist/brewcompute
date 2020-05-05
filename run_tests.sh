#!/bin/bash
set -e

printf "CHECKING SYNTAX\n"
flake8 --exclude=ui_*.py src/*.py
flake8 src/unit_tests/*.py
echo "OK"

#run unit tests
cmd='python -m unittest discover src/'
printf "\nRUNNING UNIT TESTS with $cmd\n"
$cmd
