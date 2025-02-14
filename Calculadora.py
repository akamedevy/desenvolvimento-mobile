from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (360, 640)

class Calculadora(App):
    def build(self):
        box_main = BoxLayout(orientation="vertical")
        self.texto = TextInput(text="1")
        self.botaozao = Button(text="+", on_press=self.contar)
        # botaozao.bind(on_press = self.contar)

        self.botaozinho = Button(text="-", on_press=self.diminuir)


        box_main.add_widget(self.texto)
        box_main.add_widget(self.botaozao)
        box_main.add_widget(self.botaozinho)

        return box_main
    
    def contar(self, instance):
        num = 1

        num += int(self.texto.text)
        self.texto.text = str(num)
        print(num)

    def diminuir(self, instance):
        num = 1

        num = int(self.texto.text) - 1
        self.texto.text = str(num)
        print(num)


Calculadora().run()