import math
from math import sqrt
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

        self.display = Label(text='Calculadora')
        self.display.size_hint = (1.0, 0.5)


        self.caixa_botoes = GridLayout(cols=4)

        self.botao1 = Button(text="%")
        self.botao2 = Button(text="DEL")
        self.botao3 = Button(text="C")
        self.botao4 = Button(text="/")
        self.botao5 = Button(text="1")
        self.botao6 = Button(text="2")
        self.botao7 = Button(text="3")
        self.botao8 = Button(text="+")
        self.botao9 = Button(text="4")
        self.botao10 = Button(text="5")
        self.botao11 = Button(text="6")
        self.botao12 = Button(text="-")
        self.botao13 = Button(text="7")
        self.botao14 = Button(text="8")
        self.botao15 = Button(text="9")
        self.botao16 = Button(text="*")
        self.botao17 = Button(text="**")
        self.botao18 = Button(text="0")
        self.botao19 = Button(text="√")
        self.botao20 = Button(text="=")

        # self.botao0.bind(on_press = self.zerar)
        self.botao1.bind(on_press = self.armarzenar)
        self.botao2.bind(on_press = self.deletar)
        self.botao3.bind(on_press = self.zerar)
        self.botao4.bind(on_press = self.armarzenar)
        self.botao5.bind(on_press = self.armarzenar)
        self.botao6.bind(on_press = self.armarzenar)
        self.botao7.bind(on_press = self.armarzenar)
        self.botao8.bind(on_press = self.armarzenar)
        self.botao9.bind(on_press = self.armarzenar)
        self.botao10.bind(on_press = self.armarzenar)
        self.botao11.bind(on_press = self.armarzenar)
        self.botao12.bind(on_press = self.armarzenar)
        self.botao13.bind(on_press = self.armarzenar)
        self.botao14.bind(on_press = self.armarzenar)
        self.botao15.bind(on_press = self.armarzenar)
        self.botao16.bind(on_press = self.armarzenar)
        self.botao17.bind(on_press = self.armarzenar)
        self.botao18.bind(on_press = self.armarzenar)
        self.botao19.bind(on_press = self.armarzenar)
        self.botao20.bind(on_press = self.calcular)
        # self.botao5.bind(on_press = self.armarzenar)
        # self.botao4.bind(on_press = self.calcular)

        self.caixa_botoes.add_widget(self.botao1)
        self.caixa_botoes.add_widget(self.botao2)
        self.caixa_botoes.add_widget(self.botao3)
        self.caixa_botoes.add_widget(self.botao4)
        self.caixa_botoes.add_widget(self.botao5)
        self.caixa_botoes.add_widget(self.botao6)
        self.caixa_botoes.add_widget(self.botao7)
        self.caixa_botoes.add_widget(self.botao8)
        self.caixa_botoes.add_widget(self.botao9)
        self.caixa_botoes.add_widget(self.botao10)
        self.caixa_botoes.add_widget(self.botao11)
        self.caixa_botoes.add_widget(self.botao12)
        self.caixa_botoes.add_widget(self.botao13)
        self.caixa_botoes.add_widget(self.botao14)
        self.caixa_botoes.add_widget(self.botao15)
        self.caixa_botoes.add_widget(self.botao16)
        self.caixa_botoes.add_widget(self.botao17)
        self.caixa_botoes.add_widget(self.botao18)
        self.caixa_botoes.add_widget(self.botao19)
        self.caixa_botoes.add_widget(self.botao20)
        # self.caixa_botoes.add_widget(self.botao5)

        layout.add_widget(self.display)
        layout.add_widget(self.caixa_botoes)

        return layout
    
    def zerar(self, event):
        self.display.text = ""

        
    def armarzenar(self, event):
        self.display.text +=  event.text

    def calcular(self, event):

        if "√" in self.display.text:
            numero = float(self.display.text.replace("√", ""))
            resultado = math.sqrt(numero)
            self.display.text = str(resultado)

        conta = eval(str(self.display.text))
        self.display.text = str(conta)

    def deletar(self, event):
        text = str(self.display.text)
        self.display.text = text[:-1]

if __name__ == "__main__":
    MyCalc().run()
