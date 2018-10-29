#!/bin/env python
import os
import PySimpleGUI as sg
import random
import time
import webbrowser
import google.cloud as gc
from google.cloud import texttospeech
import babel

class voice_branch():
    def __init__(self, name):
        self.name = name
        self.voice_types = []
        self.genders = []
        self.options = []

    def add_gender(self, gender):
        if gender not in self.gender:
            self.gender.append(gender)

    def add_voice_type(self, voice_type):
        if voice_type not in self.voice_types:
            self.voice_types.append(voice_type)

    def add_options(self, option):
        if option not in self.options:
            self.options.append(option)

class google_tts():

    def __init__(self):
        # set OS ENV var for the Google authentication token 
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\secure\auth.json'
        self.colours = ['GreenTan', 
            'LightGreen',
            'BluePurple',
            'Purple',
            'BlueMono',
            'GreenMono',
            'BrownBlue',
            'BrightColors',
            'NeutralBlue',
            'Kayak',
            'SandyBeach',
            'TealMono']
        self.debug = True

    def debug_print(self, *args):
        if self.debug:
            try:
                print(''.join(args), flush=True)
            except:
                print(args, flush=True)

    def synth_text(self, values):
        input_text = texttospeech.types.SynthesisInput(text=values['input_text'])
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-GB',
            name='en-GB-Wavenet-B',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3,
            speaking_rate=(values['speed']/100.0),
            pitch=values['pitch'])
        response = self.client.synthesize_speech(input_text, voice, audio_config)
        # The response's audio_content is binary.
        with open(values['output'], 'wb') as out:
            out.write(response.audio_content)
            sg.PopupAutoClose('Audio content written to file "{}"'.format(values['output']), no_titlebar=True, 
                                auto_close_duration=3, button_type=sg.POPUP_BUTTONS_NO_BUTTONS)

    def set_form_layout(self):
        self.layout = [
            [sg.Text('Google Cloud Text-to-Speech', size=(35, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Text to speak:'),
                sg.Frame(layout=[
                    [sg.Radio('text', "input_type", default=True),
                    sg.Radio('ssml', "input_type")]
                ], title='Input text type', tooltip='Choose input text type'),
                sg.Text(' '  * 60),
                sg.RButton('Google API', key='API', size=(12,2))],
            [sg.Multiline(default_text='Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 32 voices, ' + \
                                        'available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and ' + \
                                        'Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, ' + \
                                        'you can create lifelike interactions with your users, across many applications and devices.', key='input_text',size=(90, 15)),
            ],
            [sg.Text('Language / locale', size=(27, 1)),
                sg.Text('Voice type', size=(27, 1)),
                sg.Text('Voice option / gender', size=(27, 1))],
            [sg.InputCombo(self.languages, key='language',size=(27, 1)),
                sg.InputCombo(['Basic', 'WaveNet'], key='voice_type', size=(27, 1)),
                sg.InputCombo(['A - FEMALE', 'B - MALE', 'C - FEMALE', 'D - MALE'], key='voice_option', size=(27, 1))],      
            [sg.Frame(layout=[[sg.Slider(range=(25, 400), key="speed", orientation='h', size=(25, 20), default_value=100)]], title='Speed'),
                sg.Frame(layout=[[sg.Slider(range=(-20, 20), key="pitch", orientation='h', size=(25, 20), default_value=0)]], title='Pitch')],
            [sg.Text('_'  * 95)],
            [sg.Text('Choose a filename to save output as:', size=(35, 1))],
            [sg.InputText(os.path.join(os.getcwd(),'output.mp3'), key='output',size=(80, 1)), 
            sg.SaveAs(target='output',file_types=(("MP3 Files", "*.mp3"),))],
            [sg.RButton('TTS',tooltip='Click to synthesize', size=(50,2)), sg.Text(' '  * 30), sg.Exit(size=(10, 2))],
            [sg.RButton('Debug',tooltip='Check values', size=(50,2))]
        ]

    def unpack_api_data(self):
        # dict to keep track of all languages and locales from API
        self.locales = {}
        # list to only keep track of unique languages for the form
        self.languages = []
        # create a tree of the languages and the options used for the GUI, 
        # i.e. list of keys (locales) that links to a list of available voice types, genders and multiple options for that voice type
        self.voice_tree = {}
        # API call to get full list of supported voices
        self.api_voices = self.client.list_voices()
        # loop through each voice and identify the following:
        # - locale code
        # - language (used only in disply, backwards link to locale code)
        # - voice type (within each language there are types which can be various options of gender)        
        for voice in self.api_voices.voices:
            # grab the voice's name. e.g.: en-GB-Standard-A
            self.debug_print('{}-{}'.format(voice.name, texttospeech.enums.SsmlVoiceGender(voice.ssml_gender).name))
            # languages is a list but only 1 item
            # grab language code and convert to a display friendly language name
            # Example: "en-GB" -> "English (United Kingdom)"
            language_code = voice.language_codes[0]
            # check if it exists in our voice tree, if not add it
            if language_code not in self.voice_tree:
                self.voice_tree[language_code] = voice_branch(voice.name)
            # convert language code to babel friendly code. Example: "en_GB" = "en-GB"
            babel_locale_code = babel.Locale.parse(language_code.replace('-','_'))
            # check if it exists in the dict or else add it in its original form e.g. en-US
            if language_code not in self.locales:
                # store the key as its original form not babels form
                self.locales[language_code] = babel_locale_code.get_display_name('en')
                # add it to languages as well
                if self.locales[language_code] not in self.languages:
                    self.languages.append(self.locales[language_code])
            #self.debug_print('Supported language: {} -> {}'.format(language_code, self.locales[language_code]))
            # determine the voice type e.g. Wavenet or Standard
            if 'wavenet' in voice.name.lower():
                self.voice_tree[language_code].add_voice_type('Wavenet')
            else:
                self.voice_tree[language_code].add_voice_type('Standard')
            # Retrieve the Voice Gender
            # self.debug_print('Voice Gender: {} = {}'.format(
            #     voice.ssml_gender, texttospeech.enums.SsmlVoiceGender(voice.ssml_gender).name))
            # # Display the natural sample rate hertz for this voice. Example: 24000
            # self.debug_print('Natural Sample Rate Hertz: {}\n'.format(
            # voice.natural_sample_rate_hertz))
        # sort language list
        self.languages.sort()


    def main(self):
        # set a random look and feel to spice things up
        sg.ChangeLookAndFeel(random.choice(self.colours))
        # inform the user that the data is being retrieved from Google
        sg.PopupAutoClose("Retrieving data from Google", no_titlebar=True, auto_close_duration=2, button_type=sg.POPUP_BUTTONS_NO_BUTTONS)
        # make the Google API call to create the client
        self.client = texttospeech.TextToSpeechClient()
        # retrieve and unpack the data from the client
        self.unpack_api_data()
        # design and open our window and show all the options to the user
        self.set_form_layout()
        window = sg.Window('Google Cloud Text-to-Speech', default_element_size=(40, 1), grab_anywhere=False).Layout(self.layout)
        try:
            # enter an indefinte loop to keep the form open and the user can interact with it, we can then check the button presses
            while True:
                button, values = window.ReadNonBlocking()
                # check which button was clicked
                if button == 'Exit':
                    break
                elif button == 'API':
                    webbrowser.open('https://cloud.google.com/text-to-speech/')
                elif button == 'TTS':
                    #sg.Popup('The button clicked was "{}"'.format(button),
                    #    'The values are', values)
                    self.synth_text(values)
                elif button == 'Debug':
                    # retrieve locale code from chosen language
                    for key in self.locales:
                        if values['language'] == self.locales[key]:
                            self.debug_print("Language / local: {} = {}".format(values['language'], key))
                            break
                    # we should now have the locale code, list the available voices
                    #for voice in self.api_voices.voices:
                        
                elif button is not None:
                    self.debug_print(button, values)
                # if for some reason there is nothing on the form
                if values is None:
                    break
                # add a small sleep so the form can keep checking for updates
                time.sleep(.1)
        except Exception as e:
            sg.PopupError('Unexpected error occurred: "{}"'.format(e), no_titlebar=True)
        finally:
            window.CloseNonBlocking()

if __name__=='__main__':
    # create instance of the google tts form
    tts_google = google_tts()
    # call it's main function
    tts_google.main()