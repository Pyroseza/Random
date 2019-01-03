#!/bin/env python

# try importing the modules that do not come with Python by default 
# check if it is installed by importing the modules
try:
    from google.cloud import texttospeech
    import PySimpleGUI as sg
    import babel
    #print('\nAll modules installed successfully, have fun! d^o^b')
except Exception as e:
    # something is wrong with the imports try installing them
    import os
    # set the proxy
    os.environ['HTTPS_PROXY'] = r'http://ep.threatpulse.net:80'
    # install from the requirements.txt file
    os.system('pip install -U -r requirements.txt')

# the modules should be fine now...
try:
    from google.cloud import texttospeech
    import PySimpleGUI as sg
    import babel
except Exception as e:
    print('\nNot good, failed to import dependencies!')
    print(e)
    import sys
    sys.exit(1)

    
# if it got here then everything seems fine
import os
import random
import time
import webbrowser
import sys, traceback
# these need to be installed manually
from google.cloud import texttospeech
import PySimpleGUI as sg
import babel

# this is the main class for the project it contains both GUI code and API calls.
# it uses the PySimpleGUI module for GUI code which is already a wrapper class to speed up GUI dev
# and it makes calls to the Google Cloud API to fetch a list of voices that which can be used to synthesize text

class google_tts():
    def __init__(self, debug=False):
        # set OS ENV var for the Google authentication token
        if os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is None:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\secure\auth.json'
        # set the proxy
        os.environ['HTTPS_PROXY'] = r'http://ep.threatpulse.net:80'
        self.debug = debug
        self.selected_options = {}
        self.selected_options['language_locale'] = ''
        self.selected_options['voice_type'] = ''
        self.selected_options['voice_option'] = ''
        self.default_text = 'Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 32 voices, ' + \
                            'available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and ' + \
                            'Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, ' + \
                            'you can create lifelike interactions with your users, across many applications and devices.'
        self.default_output = os.path.join(os.getcwd(),'output.mp3')

    def debug_print(self, *args):
        if self.debug:
            try:
                print(''.join(args), flush=True)
            except:
                pass

    def synthesize(self, values):
        locale_code = self.convert_lang_to_locale(values['language_locale'])
        voice_type = values['voice_type']
        voice_option = values['voice_option'].split('-')
        voice_name='{}-{}-{}'.format(locale_code,voice_type,voice_option[0])
        if values['input_type_text'] == True:
            input_text = texttospeech.types.SynthesisInput(text=values['input'])
        elif values['input_type_ssml'] == True:
            input_text = texttospeech.types.SynthesisInput(ssml=values['input'])
        for gender in texttospeech.enums.SsmlVoiceGender:
            if gender.name == voice_option[1]:
                ssml_gender = gender
                break
        self.debug_print('language_locale:', locale_code)
        self.debug_print('voice_type:', voice_type)
        self.debug_print('voice_option:', voice_option)
        self.debug_print('voice_name:', voice_name)
        self.debug_print('ssml_gender:', ssml_gender)

        voice = texttospeech.types.VoiceSelectionParams(
            #language_code='en-GB',
            language_code=locale_code,
            #name='en-GB-Wavenet-B',
            name=voice_name,
            #ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
            ssml_gender=ssml_gender)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3,
            speaking_rate=(values['speed']/100.0),
            pitch=values['pitch'])
        response = self.client.synthesize_speech(input_text, voice, audio_config)
        # The response's audio_content is binary.
        with open(values['output'], 'wb') as out:
            out.write(response.audio_content)
            sg.PopupQuick('Audio content written to file "{}"'.format(values['output']), no_titlebar=True, button_type=sg.POPUP_BUTTONS_NO_BUTTONS)

    def set_form_layout(self):
        self.layout = [
            [sg.Text('Google Cloud Text-to-Speech', size=(38, 1), justification='center', font=('Helvetica', 25), relief=sg.RELIEF_RIDGE)],
            [sg.Frame(layout=[
                [sg.Radio('text', 'input_type', key='input_type_text', default=True),
                sg.Radio('ssml', 'input_type', key='input_type_ssml')]
            ], title='Input type', tooltip='Choose input type'),
            sg.Text(' '  * 110),
            sg.Button('Google API', key='API', size=(12,2))],
            [sg.Multiline(default_text=self.default_text, key='input', size=(100, 15), do_not_clear=True),
            ],
            [sg.Text('Language / locale', size=(25, 1)),
                sg.Text(' '  * 17),
                sg.Text('Voice type', size=(15, 1)),
                sg.Text(' '  * 20),
                sg.Text('Voice option / gender', size=(18, 1))],
            [sg.InputCombo(self.languages, key='language_locale',size=(25, 1),change_submits=True, readonly=True),
                sg.Text(' '  * 20),
                sg.InputCombo(['--choose locale--'], key='voice_type', size=(15, 1), change_submits=True, readonly=True),
                sg.Text(' '  * 20),
                sg.InputCombo(['--choose voice type--'], key='voice_option', size=(15, 1), readonly=True)],
            [sg.Frame(layout=[[sg.Slider(range=(25, 400), key='speed', orientation='h', size=(29, 20), default_value=100)]], title='Speed'),
                sg.Frame(layout=[[sg.Slider(range=(-20, 20), key='pitch', orientation='h', size=(29, 20), default_value=0)]], title='Pitch')],
            [sg.Text('_'  * 102)],
            [sg.Text('Choose a location and filename to save the output mp3 as:', size=(50, 1))],
            [sg.InputText(self.default_output, key='output',size=(91, 1), do_not_clear=True),
            sg.FileSaveAs(target='output', file_types=(('MP3 Files', '*.mp3'),))],
            [sg.Button('Synthesize', tooltip='Click to synthesize', size=(18,2)),
            sg.Button('Play', tooltip='Click to play', size=(18,2)),
            sg.Button('Open', tooltip='Click to open output location', size=(18,2)),
            sg.Text(' '  * 10),
            sg.Button('Reset', tooltip='Click to reset values', size=(10,2)),
            sg.Exit(size=(10, 2))]
        ]

    def unpack_api_data(self):
        # dict to keep track of all languages and locales from API
        self.locales = {}
        # list to only keep track of unique languages for the form
        self.languages = []
        # create a tree of the languages and the options used for the GUI,
        # i.e. list of keys (locales) that links to a list of available voice types, genders and multiple options for that voice type
        self.voice_list = []
        # API call to get full list of supported voices
        self.api_voices = self.client.list_voices()
        # loop through each voice and identify the following:
        # - locale code
        # - language (used only in disply, backwards link to locale code)
        # - voice type (within each language there are types which can be various options of gender)
        for voice in self.api_voices.voices:
            # grab the voice's name. e.g.: en-GB-Standard-A and add the gender to the option Male = en-GB-Standard-A-Male
            voice_formatted = '{}-{}'.format(voice.name, texttospeech.enums.SsmlVoiceGender(voice.ssml_gender).name)
            self.debug_print(voice_formatted)
            self.voice_list.append(voice_formatted)
            # languages is a list but only 1 item that I can see
            language_code = voice.language_codes[0]
            # convert language code to babel friendly code. Example: 'en-GB' => 'en_GB'
            babel_locale_code = babel.Locale.parse(language_code.replace('-','_'))
            # check if it exists in the dict or else add it in its original form e.g. en-GB
            if language_code not in self.locales:
                # store the key as its original form not babels form
                # grab language code and convert to a display friendly language name
                # store this as the value, example: 'en-GB' -> 'English (United Kingdom)'
                self.locales[language_code] = babel_locale_code.get_display_name('en')
                # add it to languages as well, used in the GUI
                if self.locales[language_code] not in self.languages:
                    self.languages.append(self.locales[language_code])
            # update the default text to the correct amount of voices
        self.default_text = 'Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with {} voices, '.format(len(self.voice_list)) + \
                'available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and ' + \
                'Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, ' + \
                'you can create lifelike interactions with your users, across many applications and devices.'
        # sort language list
        self.languages.sort()

    def convert_lang_to_locale(self,language_code):
        locale_code = ''
        for key in self.locales:
            if language_code == self.locales[key]:
                self.debug_print('Language / local: {} = {}'.format(language_code, key))
                locale_code = key
                break
        return locale_code

    def get_voice_types(self, language_code):
        # convert chosen language to locale code
        locale_code = ''
        voice_types = []
        self.selected_options['language_locale'] = self.convert_lang_to_locale(language_code)
        if self.selected_options['language_locale'] is not '':
            # we have a locale code
            # now get get a list of voice types
            for voice in self.voice_list:
                if self.selected_options['language_locale'] in voice:
                    # strip the locale code and voice option from the list
                    # en-GB-Standard-A-Male => Standard
                    voice_split = voice.split('-')
                    voice_type = voice_split[2]
                    if voice_type not in voice_types:
                        voice_types.append(voice_type)
        else:
            return ['--choose locale--']
        self.selected_options['voice_type'] = voice_types[0]
        return voice_types

    def get_voice_options(self, voice_type=''):
        if voice_type is '':
            voice_type = self.selected_options['voice_type']
        else:
            self.selected_options['voice_type'] = voice_type
        voice_options = []
        for voice in self.voice_list:
            if self.selected_options['language_locale'] in voice:
                if self.selected_options['voice_type'] in voice:
                    # strip the locale code and voice type from the list
                    # en-GB-Standard-A-Male => A-Male
                    voice_split = voice.split('-')
                    voice_option = '{}-{}'.format(voice_split[3], voice_split[4])
                    if voice_option not in voice_options:
                        voice_options.append(voice_option)
        self.selected_options['voice_option'] = voice_options[0]
        return voice_options

    def set_defaults_options_on_form(self, window):
        if self.set_defaults == True:
            # set the input text type and
            window.FindElement('input').Update(value=self.default_text)
            # set the input back to text
            window.FindElement('input_type_text').Update(value=True)
            # set selected language / locale to British English
            self.selected_options['language_locale'] = 'English (United Kingdom)'
            # select the item in the dropdown to the chosen language
            window.FindElement('language_locale').Update(set_to_index=self.languages.index(self.selected_options['language_locale']))
            # retrieve the list of voice types for the chosen language / locale
            voice_types = self.get_voice_types(self.selected_options['language_locale'])
            voice_types.sort()
            # update the voice types drop down with the new list
            window.FindElement('voice_type').Update(values=voice_types)
            # set the selected voice type to the Wavenet type
            self.selected_options['voice_type'] = 'Wavenet'
            # select the item in the dropdown to the chosen voice type
            window.FindElement('voice_type').Update(set_to_index=voice_types.index(self.selected_options['voice_type']))
            # retrieve the voice options for the chose language / locale and the chosen voice type
            voice_options = self.get_voice_options()
            voice_options.sort()
            # update the drop down the new list
            window.FindElement('voice_option').Update(values=voice_options)
            # set the selected voice option to the first Male option
            self.selected_options['voice_option'] = 'B-MALE'
            # select the item in the dropdown to the chosen voice option
            window.FindElement('voice_option').Update(set_to_index=voice_options.index(self.selected_options['voice_option']))
            # set the speed slider
            window.FindElement('speed').Update(value=100)
            # set the pitch slider
            window.FindElement('pitch').Update(value=0)
            # set the output location
            window.FindElement('output').Update(self.default_output)
            self.set_defaults = False

    def main(self):
        # set a random look and feel to spice things up
        # sg.ChangeLookAndFeel(random.choice(self.colours))
        # CDK colour scheme
        colours = ['#82C600', '#509E2F', '#FFFFFF', '#000000', '#939598']
        sg.SetOptions(background_color=colours[0],
           text_element_background_color=colours[0],
           element_background_color=colours[0],
           scrollbar_color=colours[1],
           input_elements_background_color=colours[2],
           text_color=colours[3],
           button_color=('white', colours[1]))
        # inform the user that the data is being retrieved from Google
        sg.PopupQuick('Retrieving data from Google', no_titlebar=True, button_type=sg.POPUP_BUTTONS_NO_BUTTONS)
        # make the Google API call to create the client
        self.client = texttospeech.TextToSpeechClient()
        # retrieve and unpack the data from the client
        self.unpack_api_data()
        # design and open our window and show all the options to the user
        self.set_form_layout()
        window = sg.Window('Google Cloud Text-to-Speech', no_titlebar=False, default_element_size=(40, 1), grab_anywhere=False).Layout(self.layout)
        self.set_defaults = True
        try:
            # enter an indefinte loop to keep the form open and the user can interact with it, we can then check the button presses
            while True:
                event, values = window.Read(timeout=100)
                self.set_defaults_options_on_form(window)
                # check which button was clicked
                if event == 'Exit':
                    break
                elif event == 'API':
                    webbrowser.open('https://cloud.google.com/text-to-speech/')
                elif event == 'language_locale':
                    self.debug_print(event, values)
                    voice_types = self.get_voice_types(values['language_locale'])
                    window.FindElement('voice_type').Update(values=voice_types)
                    voice_options = self.get_voice_options()
                    window.FindElement('voice_option').Update(values=voice_options)
                elif event == 'voice_type':
                    self.debug_print(event, values)
                    voice_options = self.get_voice_options(values['voice_type'])
                    window.FindElement('voice_option').Update(values=voice_options)
                elif event == 'SaveAs':
                    if values['output'].endswith('.mp3') == False:
                        output_file = values['output'] + '.mp3'
                        window.FindElement('output').Update(value=voice_options)
                elif event == 'Reset':
                    self.set_defaults = True
                    self.set_defaults_options_on_form(window)
                elif event == 'Open':
                    try:
                        full_path = values['output']
                        file_index = full_path.index(full_path.split(os.path.sep)[-1])
                        self.debug_print(full_path, full_path.split(os.path.sep), full_path.split(os.path.sep)[-1], file_index, full_path[:file_index])
                        webbrowser.open(full_path[:file_index])
                    except:
                        sg.Popup('Unable to open the output location: "{}"'.format(values['output']))
                elif event == 'Play':
                    try:
                        if os.path.exists(values['output']):
                            webbrowser.open(values['output'])
                        else:
                            sg.Popup('You need to first create the file at location: \n"{}"'.format(values['output']))
                    except Exception as e:
                        sg.Popup('An error occurred trying to play the file at location: "{}"\n{}'.format(values['output'], e))
                elif event == 'Synthesize':
                    try:
                        self.synthesize(values)
                    except Exception as e:
                        sg.Popup('Unable to synthesize input: "{}"'.format(e))
                if event is sg.TIMEOUT_KEY:
                    update = False
                    # fix some things on the form
                    if values['output'].endswith('.mp3') == False:
                        output_file = values['output'] + '.mp3'
                        update = True
                    # in Windows for some reason the file path is return with forward slashes,
                    # rather just use the correct OS path separator, if *nix based it will stay forward slash
                    if '/' in values['output']:
                        output_file = values['output'].replace('/', os.path.sep)
                        update = True
                    if update == True:
                        window.FindElement('output').Update(value=output_file)
                elif event is not None and event is not sg.TIMEOUT_KEY:
                    self.debug_print(event, values)
                # if for some reason there is nothing on the form
                if values is None:
                    break
        except Exception as e:
            sg.PopupError('Unexpected error occurred: "{}"'.format(e), no_titlebar=True)
            traceback.print_exc(file=sys.stdout)
        finally:
            window.Close()

if __name__=='__main__':
    # create instance of the google tts form
    tts_google = google_tts()
    # call it's main function
    tts_google.main()
