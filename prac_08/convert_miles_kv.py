from kivy.app import App
from kivy.lang import Builder
KM_CONST = 1.60934
class MileToKMConverter(App):

 def build(self):
    self.title = "Convert Miles to Kilometres"
    self.root = Builder.load_file('convert_miles_km.kv')
    return self.root
 def handle_validation(self):

    try:
      input_num = float(self.root.ids.input_miles.text)
      return input_num
    except ValueError:
      return 0
 def handle_calculate(self):

    input_num = self.handle_validation()
    result = input_num * KM_CONST
    self.root.ids.output_label.text = str(result)
 def handle_increment(self, increment):

    input_num = self.handle_validation() + increment
    self.root.ids.input_miles.text = str(input_num)
    self.handle_calculate()

MileToKMConverter().run()