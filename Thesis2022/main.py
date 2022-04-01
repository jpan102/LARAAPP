from telnetlib import DO
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from docx import *
import os
import SummarizeWORD, SummarizePDF, Questionnaire
from kivymd.app import  MDApp
import kivy
kivy.require('2.1.0') 
#Setting the App Size
Window.size = (500,700)

#Define Different screens
selectionF = ''

class Home(Screen):
    pass

class Main_Menu(Screen):
    
    def selects(self, selection):
        self.selection = selection
        selection = self.selection
        global selectionF
        selectionF = selection
    pass

class Upload(Screen):
    
    def load(self,path, filename):

        self.filename = filename[0]                     # Dito makukuha yung file
        basename = os.path.basename(self.filename)      # Dito cinonvert yung filename into variable

        if selectionF == "Summarize" :

            if 'docx' in basename:
                SummarizeWORD.summ(self,path,filename)
                print('\nThis is: ' + selectionF)
                pass
            
            elif 'pdf' in basename:
                SummarizePDF.summ(self,path,filename)
                print('This is: ' + selectionF)
                pass

            else:
                print ('Word/PDF File not detected.')
                pass

        elif selectionF == 'Questionnaire':
            Questionnaire.Quest(self,path,filename)
            print(selectionF + " Soon!!!")

        pass
class Create(Screen):
    pass

class WindowManager(ScreenManager):
    pass

Con = Builder.load_file('main.kv')


class ReviewerApp(MDApp):
    def build(self):
        return Con

if __name__ == '__main__':
    ReviewerApp().run()