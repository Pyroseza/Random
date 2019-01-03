# Python Text-to-speech using the Google Cloud API

1. Download [Python](https://www.python.org/downloads/) from the Internet (Don't use Software Center it's outdated).
2. Install Python using your local Admin user. Make sure to set the environment variable PATH to include path for the Python and Python\Scripts directories.
3. Place the JSON file containing the Google API Authentication in an easy to find location and then create a local environment variable called `GOOGLE_APPLICATION_CREDENTIALS` and set it to the location of the file.
```
    set GOOGLE_APPLICATION_CREDENTIALS=C:\secure\auth.json'
```
- **N.B. if you don't do this, then just make sure the file is at the above mentioned location and the program will set this for you.**
4. You should now be ready to just run the application.
There are 2 methods you can follow:
- I have created a batch file called "Text-to-speech.bat" which you can double click and launch.

Alternatively...

- You can go into the directory where the script is and perform the following steps:
1. hold shift and right-click in the open space
2. choose the item "Open command window here"
3. type in the following command and hit enter:
```
            python tts_google.py
```
- **N.B. Running the script the first time will install the dependencies required to run the application, this will need access to the internet, if you do not have internet access the entire application will fail to execute.**
### TODO
Bundle as an executable, requires alternative software
