from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

Window.size=(480,853)

from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
from kivymd.theming import ThemeManager
class Godv(GridLayout):
    def Ras(self):
        self.a=(int(self.input1.text)/(int(self.input2.text)))
        self.v=int(self.input3.text)/(self.a)
        self.voda=int(self.input3.text)-self.v

        self.label1.text = f'Бихромат {str(round(int(self.input3.text)/self.a,2))} ({round(int(self.input3.text)/self.a/0.061)}cm) '
        self.label2.text = f'Вода {str(round(self.voda,2))} ({round(self.voda/0.061)}cm) '

class MyApp(App):
    theme_cls=ThemeManager()
    title = 'bih'

    def build(self):
        self.theme_cls.theme_style='Dark'

        return Godv()
if __name__=='__main__':
    MyApp().run()

