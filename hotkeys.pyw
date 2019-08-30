import keyboard
import json
import os

def main():
    loadKeys()
    #keyboard.add_word_listener("/refreshKeys",main)
    keyboard.add_word_listener("/cmd",launchCMD)
    keyboard.add_word_listener("/csp",launchCSP)
    keyboard.add_word_listener("/ins",launchINS)
    keyboard.add_word_listener("/otl",launchOTL)
    keyboard.add_word_listener("/ltrrna",ltrrNa)
    keyboard.wait(hotkey="ctrl+g")

def loadKeys():
    #keyboard.unhook_all()
    with open("hotkeys.json", "r") as keyFile:
        data = json.load(keyFile)
        for d in data:
            keyboard.add_abbreviation(d["keybinding"],d["phrase"])
            if d["execute"]:
                keyboard.add_word_listener(d["keybinding"],execute)
    #print("Loaded Keys")

def execute():
    keyboard.send('enter',do_press=True,do_release=True)
    #print("Detected executable command")

def launchCMD():
    os.system("start cmd")

def launchCSP():
    os.system("start firefox https://customer.www.linkedin.com/support/")

def launchINS():
    os.system("start firefox https://cstool.www.linkedin.com/cstool/")

def launchOTL():
    os.system("start firefox go/otl")
def ltrrNa():
    keyboard.write(' N/A')
    keyboard.send('down, end')
    keyboard.write(' N/A')
    keyboard.send('down, end')
    keyboard.write(' N/A')
    keyboard.send('down, down, down, down, end') #scheduled upgrade date
    keyboard.write(' N/A')
    keyboard.send('down, end')
    keyboard.write(' N/A')
    keyboard.send('down, end')
    keyboard.write(' N/A')
    keyboard.send('down, end')
    keyboard.write(' N/A')
    keyboard.send('down, end')
    keyboard.write(' N/A')
    keyboard.send('down, end')
    keyboard.write('{ \n\n\n\n }')
    keyboard.send('up,up,tab,ctrl+b')


if __name__ == "__main__":
    main()
