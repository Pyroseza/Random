#!/bin/env python
import os
# set the proxy
#os.environ['HTTPS_PROXY'] = r'http://ep.threatpulse.net:80'
# install from the requirements.txt file
os.system('pip install -U -r requirements.txt')
# check if it is installed by importing the modules
try:
    from google.cloud import texttospeech
    import PySimpleGUI as sg
    import babel
    print('\nAll modules installed successfully, have fun! d^_^b')
except Exception as e:
    print(e)
