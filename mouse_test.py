import time
import mouse
import keyboard


class Mouse:
    def __init__(self, deviceLib):
        self.mouse = deviceLib
        self.test_coords = [(100, 100), (200, 200), (300, 300)]

    def move(self):
        for x, y in self.test_coords:
            mouse.move(x, y)
            time.sleep(0.01) # rapid input wont register without a delay


class Keyboard:
    def __init__(self, deviceLib):
        self.bored = deviceLib # yea...
        self.hotkey = "shift"
        self.state = bored.is_pressed('shift')

    def keyState(self):
        current_state = keyboard.is_pressed('shift')
        if current_state != self.state:
            self.state = current_state
            return True


G502 = Mouse(mouse)
G910 = Keyboard(keyboard)
while not G910.keyState():
    G502.move()
