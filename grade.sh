#!/usr/bin/env bash

# Set up autograder files

cp /autograder/submission/lab06.py .


python3 run_tests.py > /autograder/results/results.json
