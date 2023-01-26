import requests
import wikipedia as wikipedia
from kivy.app import App
from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.lang import Builder
Builder.load_file('frontEnd.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        #get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        #Get wikipedia page and list of image urls
        page =wikipedia.page(query)
        image_link = page.images[0]
        return image_link
    def download_image(self):
        #Dowload the image
        req = requests.get(self.get_image_link())
        imagePath ='files/image.jpg'
        with open(imagePath, 'wb') as file:
            file.write(req.content)
        return imagePath

    def set_image(self):
        #set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()