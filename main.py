import yeelight
from pynput.keyboard import Listener
import pyautogui
import threading
import time


class BulbChanger:
    """:param bulb - a yeelight bulb object with correct bulb IP"""

    def __init__(self, bulb, command):
        self.bulb = bulb
        self.command = command

        self.thread_mouse_pos()
        with Listener(on_press = self.show) as listener:
            listener.join()

    def thread_mouse_pos(self):
        thread = threading.Thread(target=self.change_brightness)
        thread.start()

    def change_brightness(self):
        while True:
            self.bulb.set_brightness(103 - pyautogui.position()[1] / 14)
            print(103 - pyautogui.position()[1] / 14)
            time.sleep(0.2)

    def show(self, key):
        try:
            if key.char == "a":
                self.bulb.set_rgb(255,0,0)
            if key.char == 'e':
                self.bulb.set_rgb(0,255,0)
            if key.char == 'i':
                self.bulb.set_rgb(0,0,255)
            if key.char == 'o':
                self.bulb.set_rgb(255,255,0)
            if key.char == 'u':
                self.bulb.set_rgb(255, 192, 203)
            if key.char == 'l':
                self.bulb.set_rgb(255, 128, 0)
            if key.char == 's':
                self.bulb.set_rgb(0, 204, 204)
            if key.char == 't':
                self.bulb.set_rgb(102, 0, 204)

        except:
            pass


if __name__ == "__main__":
    command = ""
    bulb = yeelight.Bulb("192.168.0.25")
    bulb_change = BulbChanger(bulb, "")
