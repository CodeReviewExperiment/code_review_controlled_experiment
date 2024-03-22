#!/usr/bin/env bash

find . -name 'code-review.csv' -exec python3 main.py --path {} \;
