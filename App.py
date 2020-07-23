import os
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = False
decision = False
notepad = '%windir%/system32/notepad.exe'
filename = 'not selected'
os.system('clear')
while True:
    choice = int(input(f'''
###############################################
Version: Alpha 1 ## File: {filename} 
###############################################                              
##   Welcome To The Code Automation Utility  ##
##                                           ##
##          Please choose from menu:         ##
##                                           ##
##          1 - write new file in notepad    ##
##          2 - execute code                 ##
##          3 - edit/fix code                ##
##          4 - clear screen                 ##
##          5 - exit the program             ## 
###############################################
###############################################
    
Please enter the appropriate option (1-5) : '''))
    if choice == 1:
        os.popen(f'{notepad}')
    elif choice == 2:
        time.sleep(.5)
        if file_path:
            decision = bool(int(input(f'\n\nWould you like to use same file i.e. -> {file_path}'
                                      f'\nPress 1 - YES'
                                      f'\nPress 0 - NO & select new file -> ')))
        if not decision:
            file_path = filedialog.askopenfilename()
        print(f'\n###############################################'
              f'\n##                 Output                    ##')
        execute = os.popen(f'python {file_path}').read()
        print(f'\n{execute}\n'
              f'\n##              End of Output                ##'
              f'\n###############################################')
        filename = file_path.split("/")[-1];
    elif choice == 3:
        os.popen(f'{notepad} {file_path}')
    elif choice == 4:
        os.system('clear')
    elif choice == 5:
        break