#!/bin/env python
import os
# try import the pip modules to be able to run the installs / updates
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain
# set the proxy
os.environ['HTTPS_PROXY'] = r'http://ep.threatpulse.net:80'

modules_to_install = ['google-cloud-texttospeech==0.2.0'
                    ,'PySimpleGUI==3.13.0'
                    ,'babel==2.6.0'
                    #,'playsound==1.2.2'
                    ]
# run the pip installs
for module in modules_to_install:
    failed = pipmain(['install', '-U', module])
    # check if install was successful
    # if failed == 0:
        # print('failed to run the install for "{}"'.format(module))
        # break
try:
    from google.cloud import texttospeech
    import PySimpleGUI as sg
    import babel
    from playsound import playsound
    print('\nAll modules installed successfully, have fun! d^_^b')
except Exception as e:
    print(e)