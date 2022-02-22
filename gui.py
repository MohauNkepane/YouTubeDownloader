import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.image import AsyncImage

import main


class MyGrid(GridLayout):


    def btn(self):
        btnstate = self.ids.submit.text
        url = self.ids.url.text
        self.add_widget(AsyncImage(source=main.getthumbnailurl(url)))


        """
        btnstate = self.ids.submit.text
        url = self.ids.url.text
        if (btnstate == "Preview") and (main.getthumbnail(url)):
            self.ids.submit.text = "Download"
            self.ids.pic.reload()

        else:
            print("To Download")
        """







class MainGui(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MainGui().run()
