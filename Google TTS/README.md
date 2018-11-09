# Python Text-to-speech using the Google Cloud API

01. Download [Python](https://www.python.org/downloads/) from the Internet (Don't use Software Center it's outdated).
02. Install Python using your local Admin user. Make sure to set the environment variable PATH to include path for the Python and Python\Scripts directories.
03. Now you need to install the using the setup.py script
```
    python setup.py
```
05. Place the JSON file into a easy to find location and then create a local environment variable called "GOOGLE_APPLICATION_CREDENTIALS" and set it to the location of the JSON file.
```
    export GOOGLE_APPLICATION_CREDENTIALS='C:/secure/auth.json'
```
06. In order run the application, go into the directory and run the following:
```
    python tts_google.py
```












pip install --upgrade google-cloud-texttospeech
pip install --upgrade PySimpleGUI
pip install --upgrade babel
pip install --upgrade playsound
    
    
google-cloud-texttospeech==0.2.0
PySimpleGUI==3.13.0
babel==2.6.0
playsound==1.2.2


Python >=3.6.3
Pip 


TODO
add a button to play / change TTS to save
add a button to open directory
single requirements.txt for installation
bundle as exe


Ryan.G.Thomson@cdk.com
Andrew.Titheridge@cdk.com
Ashley.Kirkbride@cdk.com
