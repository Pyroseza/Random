import os
import PySimpleGUI as sg
import random
import time
import webbrowser

colours = ['GreenTan', 
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
sg.ChangeLookAndFeel(random.choice(colours))

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

layout = [
    #[sg.Menu(menu_def, tearoff=True)],
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
                                'you can create lifelike interactions with your users, across many applications and devices.', key='input',size=(90, 15)),
    ],
    [sg.Text('Language / locale', size=(20, 1)),
        sg.Text('Voice type', size=(20, 1)),
        sg.Text('Voice name', size=(20, 1)),
        sg.Text('Audio device profile', size=(20, 1))],
    [sg.InputCombo(['English', 'German', 'French', 'Dutch'], key='language_locale',size=(20, 1)),
        sg.InputCombo(['Basic', 'WaveNet'], key='voice_type', size=(20, 1)),
        sg.InputCombo(['Standard A', 'Standard B', 'Wave A', 'Wave B'], key='voice_name', size=(20, 1)),
        sg.InputCombo(['Default', 'Smartphone', 'Headphones or earbuds'], key='device_profile', size=(20, 1))],        
    [sg.Frame(layout=[[sg.Slider(range=(25, 400), orientation='h', size=(25, 20), default_value=100)]], title='Speed'),
        sg.Frame(layout=[[sg.Slider(range=(-20, 20), orientation='h', size=(25, 20), default_value=0)]], title='Pitch')],
    [sg.Text('_'  * 95)],
    [sg.Text('Choose a filename to save output as:', size=(35, 1))],
    [sg.InputText(os.path.join(os.getcwd(),'output.mp3'), key='output',size=(80, 1)), 
     sg.SaveAs(target='output',file_types=(("MP3 Files", "*.mp3"),))],
    [sg.RButton('TTS',tooltip='Click to synthesize', size=(50,2)), sg.Text(' '  * 32), sg.Exit(size=(10, 2))]
]

window = sg.Window('Google Cloud Text-to-Speech', default_element_size=(40, 1), grab_anywhere=False).Layout(layout)

while True:
    button, values = window.ReadNonBlocking()
    # did the user exit
    if values is None or button == 'Exit':
        break
    # check which button was clicked
    if button == 'API':
        webbrowser.open('https://cloud.google.com/text-to-speech/')
    elif button == 'TTS':
        sg.Popup('Title',
             'The results of the window.',
             'The button clicked was "{}"'.format(button),
             'The values are', values)
    elif button is not None:
        print(button, values)
    # add a small sleep so the form can keep checking for updates
    time.sleep(.01)
print(button, values)
window.CloseNonBlocking()