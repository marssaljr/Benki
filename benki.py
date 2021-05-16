#!/usr/bin/python3
import PySimpleGUI as sg
import pyautogui as pag

layout = [[sg.Multiline('Cursor position will appear here ', disabled=True, size=(20,3), key='-TEXT-')],
	  [sg.Button('Get'), sg.Exit()]]


window = sg.Window('Benki').Layout(layout)
while True:
	event, values = window.Read()
	if event in (None, 'Exit'):
		break
	if event == 'Get':
		pos = pag.position()
		window['-TEXT-'].update(pos)

window.close()


