import time
from threading import Thread

import pynput
from pynput.keyboard import Key
from pynput.mouse import Button


class Spammer(Thread):
    
    def __init__(self):
        '''
        Create a new spammer
        '''
        super().__init__()
        self.is_spamming = False
        self.is_done = False
        self.delay = 0.01 # seconds
        self.key_controller = pynput.keyboard.Controller()
        self.mouse_controller = pynput.mouse.Controller()
        self.start() # launches self.run()

    def run(self):
        while not self.is_done:
            if self.is_spamming: 
                self.key_controller.tap('e')
            time.sleep(self.delay)  
            
    def on_click(self, x: int, y: int, button, pressed: bool):
        if button == Button.x1:
            self.is_spamming = pressed
            
    def on_press(self, key):
        if key == Key.delete:
            self.is_done = True
            exit()

spammer = Spammer()
            
with pynput.keyboard.Listener(on_press = spammer.on_press) as key_listener:
    with pynput.mouse.Listener(on_click = spammer.on_click) as mouse_listener:
        while not spammer.is_done:
            time.sleep(1)
            
        