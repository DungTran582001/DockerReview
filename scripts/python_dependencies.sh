#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
cd reviewdocker
pip3 install -r /requirements.txt