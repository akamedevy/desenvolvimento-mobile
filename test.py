from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        box1 = BoxLayout(orientation="horizontal", padding=[10], spacing=10)
        box2 = BoxLayout(orientation="vertical", padding=[10], spacing=10)
        # label = Label(text="meu appp")
        botao1 = Button(text="clica aqui")
        botao2 = Button(text="clica aqui")
        botao3 = Button(text="clica aqui")
        botao4 = Button(text="clica aqui")
        botao5 = Button(text="clica aqui")
        box.add_widget(box1)
        box.add_widget(box2)

        box1.add_widget(botao1)
        box1.add_widget(botao2)
        box2.add_widget(botao3)
        box2.add_widget(botao4)
        box2.add_widget(botao5)
        return box
    
MeuApp().run()