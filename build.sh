#!/bin/bash

python3 ./less2css.py
cp src/*.css ./dist
cp src/*.html ./dist
cp -r src/images ./dist

