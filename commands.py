from time import sleep as sl
from pynput.keyboard import Controller, Key
import pygetwindow as gw


class Commands:
    def __init__(self):
        self.keyboard = Controller()
        self.new_screen = None

    def scroll_down(self, screen_init, nv, html, Keys):
        try:
            sl(1)
            janela = gw.getWindowsWithTitle('Tainan Felipe | Facebook - Google Chrome')[0]
            janela.activate()
        except pygetwindow.PyGetWindowException as e:
            print(e)
            sl(4)
            try:
                janela = gw.getWindowsWithTitle('Tainan Felipe | Facebook - Google Chrome')[0]
                janela.activate()
            except Exception as e:
                print('activate() error 2')
                print(e)
        sl(0.1)
        self.keyboard.press(Key.esc)
        self.keyboard.release(Key.esc)
        while True:
            html.send_keys(Keys.END)
            sl(1.5)

            self.new_screen = nv.execute_script('return document.body.scrollHeight')

            if self.new_screen == screen_init:
                html.send_keys(Keys.HOME)
                nv.execute_script(f'window.scrollTo(0, 150)')
                break

            screen_init = self.new_screen


def remove_grupos(list_elem, list_btn):
    while True:
        for elem__ in list_elem:
            if 'Grupo' in elem__.text:
                elem_split = elem__.text.split("\n")
                print(f'{elem_split} #é um grupo#')
                list_elem.remove(elem__)
                sl(0.01)
            else:
                sl(0.01)
                continue
        if len(list_btn) == len(list_elem):
            break
        else:
            continue
