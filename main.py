from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class FirstApp(App):
    def build(self):
        return Button(text="oiii")
    
FirstApp().run()