from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from Controller import TrainTableController


class FindWithNumber(Screen):
    def __init__(self, controller):
        super(FindWithNumber, self).__init__()
        self.name = "train number search"
        self.controller: TrainTableController = controller
        self.dialog_window = Label(text="Dialog window")
        self.text_input = TextInput(text="")
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(Button(text="Enter number of the train:", disabled=True))
        main_layout.add_widget(self.text_input)
        main_layout.add_widget(Button(text="Search", on_press=self.press_search))
        main_layout.add_widget(self.dialog_window)
        self.add_widget(main_layout)

    def press_search(self, instance):
        if not self.controller.find_with_train_number_validation(self.text_input.text):
            self.dialog_window.text = "Error"
            return
        else:
            self.dialog_window.text = ""
            self.text_input.text = ""
            self.manager.current = "search result"
