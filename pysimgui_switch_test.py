import PySimpleGUI as sg
import time

using_imperial = True
exiting = False

imperial_choices = ['Inches','Yards','Miles','Feet','Pounds','Ounces','Gallon']
metric_choices = ['Millimeters','Centimeters','Meters','Kilometers','Kilograms','Grams','Liters']

imperial_layout = [[sg.Text('Enter a value:')],
          [sg.InputText(key='value')], 
          [sg.Text('Choose a metric unit to convert to:')],
          [sg.InputCombo(imperial_choices, size=(20, 5), key='imperial_choice')],
          [sg.Button('Calculate'), sg.Button('Switch'), sg.Exit()]]
          
metric_layout = [[sg.Text('Enter a value:')],
          [sg.InputText(key='value')], 
          [sg.Text('Choose an imperial unit to convert to:')],
          [sg.InputCombo(imperial_choices, size=(20, 5), key='imperial_choice')],
          [sg.Button('Calculate'), sg.Button('Switch'), sg.Exit()]]

while exiting == False:
    window = sg.Window('Imperial / Metric calculator').Layout(imperial_layout if using_imperial else metric_layout)
    while True:
        event, values = window.Read(100)
        if event is None or event == 'Exit':
            exiting = True
            break
        if event == 'Switch':
            # swap the form by changing flag and breaking out of the loop
            using_imperial =  not using_imperial
            break
        if event == 'Calculate':
            sg.Popup('Calculate was pressed!', 'value to convert is: {}'.format(values['value']), 'imperial unit to convert is: {}'.format(values['imperial_choice']))
        print(event, values)
    window.Close()
    window = None
    time.sleep(0.01)
