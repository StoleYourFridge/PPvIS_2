from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivymd.app import


class ViewTrainTableScreen(BoxLayout):
    def __init__(self,
                 max_amount_of_elements,
                 name):
        super(ViewTrainTableScreen, self).__init__()
        self.name = name
        self.max_amount_of_elements = max_amount_of_elements
        self.amount_of_elements = 0
        self.orientation = 'vertical'

    def increase_amount_of_elements(self):
        self.amount_of_elements += 1

    def is_new_screen_necessary(self):
        if self.amount_of_elements == self.max_amount_of_elements:
            return True
        return False
