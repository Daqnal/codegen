import os, sys
from kivy.resources import resource_add_path, resource_find

from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '300')

import random
import clipboard
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder


class MainUI(BoxLayout):

    leninputtext = ''
    outputtext = ''

    def plus(self):
        try:
            global leninputtext
            leninputtext = self.ids.lengthinput.text
            self.ids.lengthinput.text = str(int(leninputtext) + 1)
        except Exception as e: print(e)

    def minus(self):
        try:
            leninputtext = self.ids.lengthinput.text
            self.ids.lengthinput.text = str(int(leninputtext) - 1)
        except Exception as e: print(e)

    def copy(self):
        try:
            clipboard.copy(outputtext)
        except Exception as e: print(e)

    def generate(self):
        try:
            if self.ids.alphastate.state == 'down':
                length = int(self.ids.lengthinput.text)
                char = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0'
                pw = []
                joiner = ''

                for x in range(length):
                    y = random.choice(char.split())
                    pw.append(y)
                global final_pw
                final_pw = joiner.join(pw)
                global outputtext
                outputtext = str(final_pw)
                self.ids.outputbox.text = outputtext
            elif self.ids.symbolstate.state == 'down':
                length = int(self.ids.lengthinput.text)
                char = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) + - = [ ] \ ; | , . / ? > < ` ~ { } : 1 2 3 4 5 6 7 8 9 0 \ '
                pw = []
                joiner = ''

                for x in range(length):
                    y = random.choice(char.split())
                    pw.append(y)
                final_pw = joiner.join(pw)
                outputtext = str(final_pw)
                self.ids.outputbox.text = outputtext
            elif self.ids.pinstate.state == 'down':
                length = int(self.ids.lengthinput.text)
                char = '1 2 3 4 5 6 7 8 9 0 '
                pw = []
                joiner = ''

                for x in range(length):
                    y = random.choice(char.split())
                    pw.append(y)
                final_pw = joiner.join(pw)
                outputtext = str(final_pw)
                self.ids.outputbox.text = outputtext

            else:
                outputtext = 'b r u h'
                self.ids.outputbox.text = outputtext
        except:
            pass



class CodegenApp(App):
    def build(self):
        self.icon = 'logo.png'


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    CodegenApp().run()