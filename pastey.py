'''
Use OCR to read text off of an image in the clipboard
'''

import re
import string
import sys
import tkinter

import pytesseract
from PIL import ImageGrab


def tk_grabclipboard() -> str:
    '''
    Return the contents of the clipboard as a string

    This method uses tkinter because it comes in the Python 3 standard
    library. If you have something weird in the clipboard, the behavior
    of this method is undefined.

    Returns
    -------
    str
        The contents of the clipboard
    '''
    root = tkinter.Tk()
    root.withdraw()
    contents = root.clipboard_get()
    root.destroy()
    return contents

if IMAGE := ImageGrab.grabclipboard():
    # Create the character whitelist 
    punctuation = re.sub('(\'|")', r'\\\1', string.punctuation) # escape quotes
    char_whitelist = string.ascii_letters + string.digits + punctuation + ' '
    config = f'-c tessedit_char_whitelist="{char_whitelist}"'

    # OCR
    try:
        output_text = pytesseract.image_to_string(IMAGE, config = config)
    except TypeError:
        with sys.stderr as stderr:
            stderr.write('Clipboard contents are unreadable')
        sys.exit(1)

else:
    # Clipboard may contain text
    output_text = tk_grabclipboard()
    
# Formatting
output_text = re.sub(" +", " ", output_text)
output_text = re.sub("\n+", "\n", output_text)
output_text = output_text.strip()

print(output_text)
