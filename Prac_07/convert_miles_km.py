from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILE_CONSTANT = 1.60934


class ConvertMiles(App):

    def build(self):
        Window.size = (700, 250)
        self.title = "Convert_Miles_to_Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calc(self):
        value = self.mile_check()
        answer = value * MILE_CONSTANT
        self.root.ids.output_label.text = str(answer)

    def handle_increment(self, change):

        value = self.mile_check() + change
        self.root.ids.input_miles.text = str(value)
        self.mile_check()

    def mile_check(self):
        try:
            inpt = float(self.root.ids.input_miles.text)
            return inpt
        except ValueError:
            return 0


ConvertMiles().run()
