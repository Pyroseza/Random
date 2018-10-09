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

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Google Cloud Text-to-Speech', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE), sg.RButton('API')],
    [sg.Text('Text to speak:')],
    [sg.Multiline(default_text='Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 32 voices, ' + \
                                'available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and ' + \
                                'Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, ' + \
                                'you can create lifelike interactions with your users, across many applications and devices.', key='input',size=(80, 10))],
    [sg.Frame(layout=[
    [sg.Radio('text', "input_type", default=True, size=(10,1)), 
    sg.Radio('ssml', "input_type")]], title='Input text type', relief=sg.RELIEF_SUNKEN, tooltip='Choose input text type ')],    
    [sg.InputCombo(['English', 'Afrikaans'], size=(20, 1)),
     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
     sg.Frame('Labelled Group',[[
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
     sg.Column(column1, background_color='#F7F3EC')]])],
    [sg.Text('_'  * 80)],
    [sg.Text('Choose A File', size=(35, 1))],
    [sg.Text('Audio Output:', size=(10, 1), auto_size_text=False),
     sg.InputText('output.mp3', key='output',size=(60, 1)), 
     sg.SaveAs(target='output',file_types=(("MP3 Files", "*.mp3"),))],
    [sg.RButton('TTS',tooltip='Click to read the window'), sg.Exit()]
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