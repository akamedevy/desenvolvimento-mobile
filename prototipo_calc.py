from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
Window.size = (400,700)

class MyCalc(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.botao0 = Button(text="C")
        self.botao0.size_hint = (1.0, 0.2)

        self.display = Label(text='love #fffff')

        self.caixa_botoes = GridLayout(cols=4)

        self.botao1 = Button(text="1")
        self.botao2 = Button(text="2")
        self.botao3 = Button(text="+")
        self.botao4 = Button(text="=")

        self.botao0.bind(on_press = self.zerar)
        self.botao1.bind(on_press = self.armarzenar)
        self.botao2.bind(on_press = self.armarzenar)
        self.botao3.bind(on_press = self.armarzenar)
        self.botao4.bind(on_press = self.calcular)

        self.caixa_botoes.add_widget(self.botao1)
        self.caixa_botoes.add_widget(self.botao2)
        self.caixa_botoes.add_widget(self.botao3)
        self.caixa_botoes.add_widget(self.botao4)

        layout.add_widget(self.display)
        layout.add_widget(self.botao0)
        layout.add_widget(self.caixa_botoes)

        return layout
    
    def zerar(self, event):
        self.display.text = ""

        
    def armarzenar(self, event):
        self.display.text +=  event.text

    def calcular(self, event):
        conta = eval(str(self.display.text))
        self.display.text = str(conta)

    # def calcular(self, event):
    #     if "+" in self.display.text:
    #         numbers = self.display.text.split("+")
    #         soma = int(numbers[0]) + int(numbers[1])

    #         self.display.text = str(soma)

if __name__ == "__main__":
    MyCalc().run()
