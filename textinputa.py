from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MeuApicativo(App):
    def build(self):
        box_main = BoxLayout(orientation="vertical")
        texto = TextInput(text="1")
        botaozao = Button(text="aaaa")

        box_main.add_widget(texto)
        box_main.add_widget(botaozao)

        return box_main

MeuApicativo().run()