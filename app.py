import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Myapp(App):
    def build(self):
        return Label(text = "Hello World")

if __name__ == "__main__":
    Myapp().run()