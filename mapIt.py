#! python3
# mapIt.py - Launches a Google Map of the address entered from the command line (or the clipboard)

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from CLI
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)