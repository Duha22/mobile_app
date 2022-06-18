import socket
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    Window.clearcolor = (1, 1, 1, 1)
    def build(self):

        layout = BoxLayout(orientation='horizontal')
        text_layout = BoxLayout(orientation='horizontal',
                                size_hint=(0.5, None),
                                size=(100, 35),
                                pos_hint={'top':1, 'left':1})
        # self.txt = TextInput(text='serch...',
        #                      multiline=False,
        #                      size_hint=(None, None),
        #                      size=(100, 30),
        #                      pos_hint={'top':1, 'left':1})
        self.txt = Label(text="Serche...",
                         size_hint=(None, None),
                         size=(100, 40),
                         pos_hint={'top':1, 'left':1},
                         color=[0,0,0,1])
        btn = Button(background_normal="button.png",
                     size_hint=(None, None),
                     size=(75, 75),
                     pos_hint={'rigt':1, 'top':1})
        btn.bind(on_press=self.connect)

        text_layout.add_widget(self.txt)
        layout.add_widget(text_layout)
        layout.add_widget(btn)

        return layout

    def connect(self, instance):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.0.127', 1379))
        txt = str("connect")
        self.txt.text = txt

if __name__ == '__main__':
    app = MainApp()
    app.run()