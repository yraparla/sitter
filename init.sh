#!/usr/bin/bash

virtualenv -p python2.7 env
source env/bin/activate
STATIC_DEPS=true pip install lxml