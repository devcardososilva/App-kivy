from kivy.app import App
from kivy.uix button import BoxLayout
from kivy.uix boxlayout import boxlayout
from kivy.uix label import label

class test(app)
    def build(self):
        box = BoxLayout (orientation = 'vertical')
        button = button (text= 'botao 1')
        label = label (text= 'Texto 1')
        box.add_widget (button)
        box.add_widget (label)

        box2 = BoxLayout()
        button2 = button (text = 'Botao 2')
        label2 = label (text = 'Texto 2')
        box2.add_widget (button2)
        box2.add_widget (label2)

        box.add_widget (box2)
        return box
    
Test().run()