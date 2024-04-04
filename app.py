from kivy.app import App
from kivy.uix.button import Button

class Test(App):
    def build(self):
        return Button(text='Tchoi', color='red')

# Chamada para iniciar o aplicativo
Test().run()
