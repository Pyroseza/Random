# Python Text-to-speech using the Google Cloud API

01. Download [Python](https://www.python.org/downloads/) from the Internet (Don't use Software Center it's outdated).
02. Install Python using your local Admin user. Make sure to set the environment variable PATH to include path for the Python and Python\Scripts directories.
03. Now you need to install the dependent modules by running the `setup.py` script
```
    python setup.py
```
04. Place the JSON file containing the Google API Authentication in an easy to find location and then create a local environment variable called `GOOGLE_APPLICATION_CREDENTIALS` and set it to the location of the file.
```
    set GOOGLE_APPLICATION_CREDENTIALS=C:\secure\auth.json'
```

-    N.B. if you don't do this, then just make sure the file is at the above mentioned location and the program will set this for you.
05. In order run the application, go into the directory and run the following:
```
    python tts_google.py
```

### TODO
Bundle as an executable
