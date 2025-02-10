from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (360, 640)

class MeuApicativo(App):
    def build(self):
        box_main = BoxLayout(orientation="vertical")
        texto = TextInput(text="1")
        botaozao = Button(text="aaaa", on_press=self.contar)
        # botaozao.bind(on_press = self.contar)


        box_main.add_widget(texto)
        box_main.add_widget(botaozao)

        return box_main
    
    def contar(self, instance):
        x = 1
        print(instance)

MeuApicativo().run()