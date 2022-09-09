from pynput.keyboard import Controller as KeyboardController, Listener, KeyCode
from pynput.mouse import Controller as MouseController
import threading

keyboard = KeyboardController()
mouse = MouseController()
exit_key = KeyCode(char='~')


def on_press(key):
    if key == exit_key:
        thread.exit()
        listener.stop()
    else:
        pass


class Run(threading.Thread):
    def __init__(self):
        super(Run, self).__init__()
        self.running = True

    def run(self):
        while self.running:
            mouse.move(1920, 540)
            # keyboard.type('fuck ')

    def exit(self):
        self.running = False


thread = Run()
thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
