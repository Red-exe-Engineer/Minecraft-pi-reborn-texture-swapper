#normal stuffs
import os
run = True
print('Created by Red-exe-Engineer\nhttps://www.youtube.com/channel/UCzAOB6RwvO5PWjLsuFNJ4MQ')

#import PySimpleGUI or install it with pip
try:
    import PySimpleGUI as sg
except:
    #ask if the user wants to install PySimpleGUI
    install = ''
    while install != 'y' and install != 'n':
        install = input(('ERR: PySimpleGUI is not installed on your system.\nWould you like to install it? [y/n] '))
        if install != 'y' and install != 'n':
            print('ERR: "{}" is not a valid operation'.format(install))

    #install PySimpleGUI
    if install == 'y':
        os.system('sudo pip3 install PySimpleGUI')
        try:
            import PySimpleGUI as sg
        except:
            print('ERR: cannot import PySimpleGUI')
            run = False
    else:
        run = False

#set up GUI elements
layout = [
    [
        sg.Text('Image Folder'),
        sg.In(size=(25,1), enable_events=True, key='-FOLDER-'),
        sg.FileBrowse('Browse Files'),
        sg.Button('Swap File!')
    ],
    [
        [sg.Image(key='-IMAGE-')],
    ],
]

window = sg.Window(title='MCPI Reborn Terrain.png swapper', layout=layout, size=(700, 400))
#main loop
while run:
    event, values = window.read()

    #check if the user wants to close the window
    if event == sg.WIN_CLOSED:
        break

    if event == 'OK':
        print(event)

    #display the image
    try:
        window['-IMAGE-'].update(values['-FOLDER-'])
    except:
        if os.path.exists(values['-FOLDER-']):
            sg.Popup('ERR:', 'That\'s not an image file!')

    #start swapping
    if event == 'Swap File!':
        #check if the file is named terrain.png
        if not str.find(values['-FOLDER-'], 'terrain.png'):
            sg.Popup('WARNING','The file image you have selected','is not called terrain.png','This may cause unexpected errors')

        #check if a file is selected
        if values['-FOLDER-'] == '':
            sg.Popup('ERR:','You didn\'t select a file!')
        else:
            try:
                if os.path.exists(values['-FOLDER-']):

                    #move the terrain.png file in clients images folder to /tmp
                    if os.path.exists('/opt/minecraft-pi-reborn-client/data/images/terrain.png'):
                        os.system('sudo mv /opt/minecraft-pi-reborn-client/data/images/terrain.png /tmp')
                    else:
                        sg.Popup('ERR:','There is no terrain.png file in\n/opt/minecraft-pi-reborn-client/data/images','Skipping moving it')

                    #move the selected image to the clients images foder
                    os.system('sudo mv {} /opt/minecraft-pi-reborn-client/data/images/'.format(values['-FOLDER-']))

                    #move the original terrain.png file if it exists
                    if os.path.exists('/tmp/terrain.png'):
                        os.system('sudo mv /tmp/terrain.png {}'.format(os.path.dirname(values['-FOLDER-'])))
                    sg.Popup('Successfully swapped the image!','Thank you for using my program!',' - Wallee')
                else:
                    sg.Popup('ERR:', 'It seems your texture','pack has gone missing!')
            except:
                #incase something goes wrong XD
                sg.Popup('ERR:','Could not swap image','\'{}\''.format(values['-FOLDER-']))

    #update the image, may cause an error if the two files do not share the same name
    try:
        window['-IMAGE-'].update(values['-FOLDER-'])
    except:
        pass

#stop the program
print('The main loop has stopped, hope this was you XD')
window.close()