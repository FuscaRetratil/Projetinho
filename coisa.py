from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
<<<<<<< Updated upstream
from kivymd.uix.button.button import MDRaisedButton
from kivy.core.text import LabelBase
=======
from kivymd.uix.button.button import MDRaisedButton1
>>>>>>> Stashed changes
Window.size = (350, 550)

class ChatBot(MDApp):

    def mudar_tela(self, nome):
        screen_manager.current = nome



    def build(self):
         global screen_manager
         screen_manager = ScreenManager ()
         screen_manager.add_widget(Builder.load_file("Main.kv"))
         screen_manager.add_widget(Builder.load_file("Chats.kv"))
         return screen_manager
    

    
    




if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()
