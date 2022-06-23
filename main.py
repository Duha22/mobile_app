import socket
from kivy.app import App
# from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Gui(BoxLayout):
    label_widget = ObjectProperty()
    flag_connection = 0

    def connect_server(self):
        if self.flag_connection == 0:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('192.168.0.127', 1379))
            self.client.send("connected".encode('utf-8'))
            self.label_widget.text = 'Connected'
            self.flag_connection = 1
        elif self.flag_connection == 1:
            self.client.send("disconnected".encode('utf-8'))
            self.client.close()
            self.label_widget.text = 'Disconnected'
            self.flag_connection = 0
    def pause(self):
        self.client.send("pause".encode('utf-8'))

class MainApp(App):
    # Window.clearcolor = (1, 1, 1, 1)
    def build(self):
        return Gui()


if __name__ == '__main__':
    MainApp().run()