import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.image import Image
import main


class MyGrid(GridLayout):
    picture = StringProperty("thumb.png")

    def btn(self):
        btnstate = self.ids.submit.text
        if (btnstate == "Preview") and (main.getthumbnail("https://www.youtube.com/watch?v=cv7dht7pb6s")):
            self.ids.submit.text = "Download"
            self.ids.pic.source = self.picture
        else:
            print("To Download")







class MainGui(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MainGui().run()
