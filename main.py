import socket
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Gui(BoxLayout):
    pass

class MainApp(App):
    # Window.clearcolor = (1, 1, 1, 1)
    def build(self):
        return Gui()

    # def connect(self, instance):
    #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     client.connect(('192.168.0.127', 1379))
    #     txt = str("connect")
    #     self.txt.text = txt

if __name__ == '__main__':
    MainApp().run()