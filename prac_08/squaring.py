from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
__author__ = 'Lindsay Ward'
class SquareNumberApp(App):

   def build(self):
    Window.size = (300, 200)
    self.title = "Square Number"
    self.root = Builder.load_file('squaring.kv.kv')
    return self.root
   def handle_calculate(self, value):

    result = value ** 2
    self.root.ids.output_label.text = str(result)
SquareNumberApp().run()